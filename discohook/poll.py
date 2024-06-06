import asyncio
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union, Tuple

from .emoji import PartialEmoji
from .enums import PollLayoutType
from .user import User

if TYPE_CHECKING:
    from .client import Client
    from .message import Message


class PollMedia:
    """
    The question of the poll. Only text is supported.

    Properties
    ----------
    text: Optional[:class:`str`]
        The text of the media.
    emoji: Optional[:class:`PartialEmoji`]
        The emoji of the media.
    """

    def __init__(self, data: Dict[str, Any]):
        self._data = data

    @classmethod
    def from_str(cls, text: str) -> "PollMedia":
        return cls({"text": text})

    @property
    def text(self) -> Optional[str]:
        return self._data.get("text")

    @property
    def emoji(self) -> Optional[PartialEmoji]:
        return self._data.get("emoji")

    def to_dict(self) -> Dict[str, Any]:
        return self._data


class PollAnswer:
    """
    An answer to a poll.

    Properties
    ----------
    answer_id: :class:`int`
        The ID of the answer.
    poll_media: Optional[:class:`PollMedia`]
        The media of the answer.

    """

    def __init__(self, data: Dict[str, Any]):
        self._data = data

    @classmethod
    def new(cls, answer_id: int, media: Union[str, PollMedia]) -> "PollAnswer":
        """
        Create a new poll answer.
        Parameters
        ----------
        answer_id: :class:`int`
            The ID of the answer.
        media: Union[:class:`str`, :class:`PollMedia`]
            The media of the answer.

        Returns
        -------
        :class:`PollAnswer`
            The newly created poll answer.

        """
        if isinstance(media, str):
            media = PollMedia.from_str(media)
        return cls({"answer": answer_id, "poll_media": media.to_dict()})

    @property
    def id(self) -> int:
        return self._data["answer_id"]

    @property
    def media(self) -> PollMedia:
        return PollMedia(self._data["poll_media"])

    def to_dict(self) -> Dict[str, Any]:
        return self._data


class PollAnswerCount:
    """
    Represents the count of an answer in a poll.

    Properties
    ----------
    answer_id: :class:`int`
        The ID of the answer.
    count: :class:`int`
        The count of the answer.
    """

    def __init__(self, data: Dict[str, Any]):
        self._data = data

    @property
    def answer_id(self) -> int:
        return self._data["answer_id"]

    @property
    def count(self) -> int:
        return self._data["count"]

    def me_voted(self) -> bool:
        return self._data["me_voted"]


class Poll:
    """
    A poll object.

    Properties
    ----------
    question: Optional[:class:`str`]
        The question of the poll.
    answers: Optional[List[:class:`PollAnswer`]]
        The answers to the poll.
    expiry: Optional[:class:`int`]
        The expiry time of the poll.
    allow_multiselect: :class:`bool`
        Whether the poll allows multiple answers.
    layout: :class:`PollLayoutType`
        The layout of the poll.
    """

    def __init__(self, data: Dict[str, Any]):
        self._data = data
        self._message_id = None
        self._channel_id = None
        self._client = None

    @classmethod
    def _from_message(cls, client: "Client", message: "Message") -> "Poll":
        data = message.data["poll"]
        poll = cls(data)
        poll._client = client
        poll._message_id = message.id
        poll._channel_id = message.channel_id
        return poll

    @classmethod
    def new(
        cls,
        question: str,
        *answers: PollAnswer,
        expiry: Optional[int] = None,
        allow_multiselect: bool = False,
        layout: int = PollLayoutType.default
    ) -> "Poll":
        assert question, "Polls must have a question."
        assert len(question) <= 300, "Poll question must be less than 300 characters."
        assert len(answers) > 0, "Polls must have at least one answer."
        assert len(answers) <= 10, "Polls can have at most 10 answers."
        for answer in answers:
            assert (
                len(answer.media.text) <= 55
            ), "Poll answer must be less than 55 characters."
        return cls(
            {
                "question": {"text": question},
                "answers": [ans.to_dict() for ans in answers],
                "expiry": expiry,
                "allow_multiselect": allow_multiselect,
                "layout_type": layout,
            }
        )

    @property
    def question(self) -> Optional[str]:
        return self._data.get("question")

    @property
    def answers(self) -> Optional[List[PollAnswer]]:
        ans = self._data.get("answers")
        if ans is not None:
            return [PollAnswer(data) for data in ans]
        return None

    @property
    def expiry(self) -> Optional[int]:
        return self._data.get("expiry")

    @property
    def allow_multiselect(self) -> bool:
        return self._data.get("allow_multiselect", False)

    @property
    def layout(self) -> PollLayoutType:
        return PollLayoutType(
            self._data.get("layout_type", PollLayoutType.default.value)
        )

    @property
    def is_finalized(self) -> bool:
        return self._data.get("is_finalized", False)

    @property
    def answer_counts(self) -> Optional[List[PollAnswerCount]]:

        counts = self._data.get("answer_counts")
        if counts is None:
            return None
        return [PollAnswerCount(data) for data in counts]

    def to_dict(self) -> Dict[str, Any]:
        self._data["duration"] = self._data.pop("expiry", None)
        return self._data

    async def __fetch_voters(
        self, answer_id: int, *, after: Optional[str] = None, limit: int = 25
    ) -> Tuple[int, List[User]]:
        limit = limit if limit <= 100 else 100
        params = {"limit": limit}
        assert (
            self._channel_id and self._message_id and self._client
        ), "Only polls fetched from a message can fetch voters."
        if after:
            params["after"] = after
        resp = await self._client.http.fetch_answer_voters(
            self._channel_id, self._message_id, answer_id, params=params
        )
        voters = await resp.json()
        return answer_id, [User(self._client, data) for data in voters]

    async def fetch_all_voters(self) -> Dict[int, List[User]]:
        """
        Fetch all the answers of the poll.
        Returns
        -------
        Dict[:class:`int`, List[:class:`User`]]
        """
        answers_ids = [ans.id for ans in self.answers]
        tasks = []
        for id in answers_ids:
            tasks.append(self.__fetch_voters(id))
        voters = asyncio.gather(*tasks)
        return dict(voters)

    async def fetch_voters(
        self, answer_id: int, *, after: Optional[str] = None, limit: int = 25
    ) -> List[User]:
        """
        Fetch the voters of an answer with pagination.
        Parameters
        ----------
        answer_id: :class:`int`
            The ID of the answer.
        after: Optional[:class:`str`]
            The ID of the last user fetched.
        limit: :class:`int`
            The number of users to fetch. Maximum is 100.

        Returns
        -------
        List[:class:`User`]
        """
        _, users = self.__fetch_voters(answer_id, after=after, limit=limit)
        return users

    async def end(self):
        """
        Ends the poll.
        """
        return await self._client.http.end_poll(self._channel_id, self._message_id)
