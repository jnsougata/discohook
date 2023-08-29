from aiohttp import ClientSession
from typing import List, Optional, Dict, Any, Tuple

from .errors import *
from .utils import Record, Updater, Query, time_converter


def _update_ttl(record: Record):
    if "expire_after" in record and "expire_at" in record:
        raise ValueError('expire_after and expire_at are mutually exclusive')
    if "expire_after" in record:
        record["__expires"] = time_converter(record["expire_after"])  # type: ignore
        del record["expire_after"]
    if "expire_at" in record:
        record["__expires"] = time_converter(record["expire_at"])  # type: ignore
        del record["expire_at"]


class Base:
    """
    Represents a Deta Base instance

    Parameters
    ----------
    name : str
        Name of the base
    project_id : str
        Project ID to be used for requests
    session : aiohttp.ClientSession
        External client session to be used for requests
    """
    def __init__(self, name: str, project_id: str, session: ClientSession):
        self.name = name
        self.session = session
        self.project_id = project_id
        self.root = f'https://database.deta.sh/v1/{self.project_id}/{name}'

    def __str__(self):
        return self.name

    async def close(self):
        """
        Close the client session
        """
        return await self.session.close()
    
    async def put(self, *records: Record):
        """
        Put records into the base (max 25 records at a time)

        Parameters
        ----------
        *records : Tuple[Record]
            Records to be put into the base

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Raises
        ------
        ValueError
            If no records are provided or more than 25 records are provided
        BadRequest
            If request body is invalid
        """
        if not records:
            raise ValueError('at least one record must be provided')
        if len(records) > 25:
            raise ValueError('cannot put more than 25 records at a time')
        for record in records:
            _update_ttl(record)
        resp = await self.session.put(f'{self.root}/items', json={"items": records})
        return await _raise_or_return(resp, 207)

    async def delete(self, key: str) -> Dict[str, Any]:
        """
        Delete a record from the base

        Parameters
        ----------
        key : str
            Key of the record to be deleted

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Notes
        -----
        If the key does not exist, the API will still return a 200 response with the following body:

        ``{"key": "key"}``
        """
        resp = await self.session.delete(f'{self.root}/items/{key}')
        return await resp.json()

    async def get(self, key: str) -> Dict[str, Any]:
        """
        Get a record from the base

        Parameters
        ----------
        key : str
            Key of the record to be fetched

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Raises
        ------
        ValueError
            If key is empty or None
        NotFound
            If the key does not exist in the base
        """
        if not key:
            raise ValueError('key cannot be empty')
        resp = await self.session.get(f'{self.root}/items/{key}')
        return await _raise_or_return(resp, 200)
    
    async def update(self, key: str, updater: Updater) -> Dict[str, Any]:
        """
        Update a record in the base

        Parameters
        ----------
        key : str
            Key of the record to be updated
        updater : Updater
            Object containing the update operations

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Raises
        ------
        ValueError
            If key is empty or None
        NotFound
            If the key does not exist in the base
        BadRequest
            If request body is invalid
        """
        if not key:
            raise ValueError('key cannot be empty')
        resp = await self.session.patch(f'{self.root}/items/{key}', json=updater.json())
        return await _raise_or_return(resp, 200)

    async def insert(self, record: Record) -> Dict[str, Any]:
        """
        Insert a record into the base

        Parameters
        ----------
        record : :class:`Record`
            Record to be inserted into the base

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Raises
        ------
        BadRequest
            If request body is invalid
        KeyConflict
            If the key already exists in the base
        """
        _update_ttl(record)
        resp = await self.session.post(f'{self.root}/items', json={"item": record})
        return await _raise_or_return(resp, 201)

    async def fetch(
        self,
        queries: Optional[List[Query]] = None,
        *,
        limit: Optional[int] = None,
        last: Optional[str] = None,
        sort: bool = False
    ) -> Dict[str, Any]:
        """
        Fetch records from the base

        Parameters
        ----------
        queries : List[Query] | None
            List of Query objects to be applied to the fetch operation
        limit : int | None
            Maximum number of records to be fetched (defaults to 1000)
        last : str | None
            Key of the last record fetched in the previous fetch operation
        sort : bool
            Whether to sort the results by key in descending order (defaults to False)

        Returns
        -------
        Dict[str, Any]
            Response from the API

        Raises
        ------
        BadRequest
            If request body is invalid
        """
        if queries is None:
            queries = []
        payload = {"query": [q.json() for q in queries]}
        if limit:
            payload['limit'] = limit
        if last:
            payload['last'] = last
        if sort:
            payload['sort'] = 'desc'
        resp = await self.session.post(f'{self.root}/query', json=payload)
        return await _raise_or_return(resp, 200)

    @staticmethod
    def _process_result(result: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], Optional[str]]:
        items = result.get('items') or []
        try:
            return items, result['paging']['last']
        except KeyError:
            return items, None

    async def fetch_all(self, queries: Optional[List[Query]] = None) -> List[Dict[str, Any]]:
        """
        Fetch all records from the base

        Parameters
        ----------
        queries : List[Query] | None
            List of Query objects to be applied to the fetch operation

        Returns
        -------
        List[Dict[str, Any]]
            List of records fetched from the base

        Raises
        ------
        BadRequest
            If request body is invalid
        """
        results = []
        result = await self.fetch(queries)
        items, last = self._process_result(result)
        results.extend(items)
        while last:
            result = await self.fetch(queries, last=last)
            items, last = self._process_result(result)
            results.extend(items)
        return results
