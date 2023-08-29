import re
import asyncio
from aiohttp import ClientSession, StreamReader
from urllib.parse import quote_plus
from typing import Dict, Optional, Any, Tuple

from .errors import *

MAX_UPLOAD_SIZE = 10485760  # 10MB


class Drive:
    """
    Represents a Deta Drive instance

    Parameters
    ----------
    name : str
        Name of the drive
    project_key : str
        Project key of the drive
    session : aiohttp.ClientSession
        External client session to be used for requests
    """

    def __init__(self, name: str, project_key: str, session: ClientSession):
        self.name = name
        self.session = session
        self.project_id = project_key.split('_')[0]
        self.root = f'https://drive.deta.sh/v1/{self.project_id}/{quote_plus(name)}'

    async def close(self):
        """
        Close the client session
        """
        await self.session.close()

    async def put(
        self, 
        content: bytes,
        *,
        save_as: Optional[str],
        folder: Optional[str] = None,
        content_type: Optional[str] = 'application/octet-stream',
    ) -> Dict[str, Any]:
        """
        Put a file into the drive

        Parameters
        ----------
        content : bytes
            Content of the file in bytes
        save_as : str
            Name of the file to be saved as
        folder : str | None
            Name of the folder to put the file in
        content_type : str | None
            Content type of the file

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Raises
        ------
        BadRequest
            If request body is invalid
        NotFound
            If the file is not found during chunked upload finalization
        PayloadTooLarge
            If the file size is greater than 10MB for direct upload or single chunk of chunked upload
        IncompleteUpload
            If the file is not uploaded completely during chunked upload
        """
        if folder:
            save_as = quote_plus(f'{folder}/{save_as}')
        else:
            save_as = quote_plus(save_as)
        headers = {"Content-Type": content_type}
        if not len(content) > MAX_UPLOAD_SIZE:
            resp = await self.session.post(f'{self.root}/files?name={save_as}', headers=headers, data=content)
            return await _raise_or_return(resp, 201)

        r = await self.session.post(f'{self.root}/uploads?name={save_as}', headers=headers)
        if r.status == 202:
            data = await r.json()
            upload_id, name = data['upload_id'], data['name']
            chunks = [content[i:i+MAX_UPLOAD_SIZE] for i in range(0, len(content), MAX_UPLOAD_SIZE)]
            tasks = [
                self.session.post(f"{self.root}/uploads/{upload_id}/parts?name={name}&part={i + 1}", data=chunk)
                for i, chunk in enumerate(chunks)
            ]
            gathered = await asyncio.gather(*tasks)
            status_codes = [r.status == 200 for r in gathered]
            if all(status_codes):
                resp = await self.session.patch(f"{self.root}/uploads/{upload_id}?name={name}")
                return await _raise_or_return(resp, 200)
            else:
                await self.session.delete(f"{self.root}/uploads/{upload_id}?name={name}", headers=headers)
                raise IncompleteUpload(f"Failed to upload all chunks of the file `{name}`")
        else:
            raise await _raise_or_return(r, 202)

    async def files(
        self, 
        limit: Optional[int] = None, 
        prefix: Optional[str] = None, 
        last: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get a list of files in the drive

        if no parameters are provided, names of all files in the drive are returned

        Parameters
        ----------
        limit : int | None
            Number of files to return
        prefix : str | None
            Prefix to filter files by
        last : str | None
            Last id returned in the previous request

        Returns
        -------
        Dict[str, Any]
            Response from the API
        """
        if not limit and not prefix and not last:
            init_r = await self.session.get(f'{self.root}/files')
            init_d = await init_r.json()
            last = None
            files = init_d['names']
            try:
                last = init_d['paging']['last']
            except KeyError:
                pass
            while last:
                resp = await self.session.get(f'{self.root}/files?last={last}')
                data = await resp.json()
                files.extend(data['names'])
                try:
                    last = data['paging']['last']
                except KeyError:
                    last = None
            return {'names': files}

        if not limit or limit > 1000 or limit < 0:
            limit = 1000
        url = f'{self.root}/files?limit={limit}'
        if prefix:
            url += f'&prefix={prefix}'
        if last:
            url += f'&last={last}'
        resp = await self.session.get(url)
        return await resp.json()

    async def delete(self, *names: str) -> Dict[str, Any]:
        """
        Delete files from the drive

        Parameters
        ----------
        *names : Tuple[str]
            Names of the files to delete

        Returns
        -------
        Dict[str, Any]
            Response from the API
        """
        if not names:
            raise ValueError('at least one filename must be provided')
        r = await self.session.delete(f'{self.root}/files', json={'names': list(names)})
        return await r.json()
    
    async def size_of(self, name: str) -> int:
        """
        Get the size of a file in the drive in bytes

        Parameters
        ----------
        name : str
            Name of the file to get the size of
        """
        resp = await self.session.get(f'{self.root}/files?name={name}', headers={'Range': 'bytes=0-0'})
        if resp.status != 206:
            raise NotFound(f'File `{name}` not found')
        range_header_value = resp.headers.get('Content-Range')
        pattern = re.compile(r'bytes 0-0/(\d+)')
        match = pattern.match(range_header_value)
        return int(match.group(1))

    async def get(self, name: str, *, _range: Optional[Tuple[int, int]] = None) -> StreamReader:
        """
        Get a file from the drive

        Parameters
        ----------
        name : str
            Name of the file to get
        _range : Tuple[int, int] | None
            Range of bytes to get from the remote file buffer

        Returns
        -------
        aiohttp.StreamReader
            The file content as a stream reader

        Raises
        ------
        NotFound
            If the file is not found
        BadRequest
            If the range is invalid
        """
        headers = {}
        if _range:
            start, end = _range if len(_range) == 2 else (_range[0], None)
            headers['Range'] = f'bytes={start}-{end}' if end else f'bytes={start}-'
        resp = await self.session.get(f'{self.root}/files/download?name={name}', headers=headers)
        if resp.status in (200, 206):
            return resp.content
        else:
            raise await _raise_or_return(resp)
