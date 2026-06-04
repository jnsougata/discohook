---
title: discohook.poll
---

# `discohook.poll`

## Classes

- [Poll](#class-poll)
- [PollAnswer](#class-pollanswer)
- [PollAnswerCount](#class-pollanswercount)
- [PollMedia](#class-pollmedia)

<a id="class-poll"></a>
## Poll

`discohook.poll.Poll`

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

### Method Index

- [end](#poll-end)
- [fetch_all_voters](#poll-fetch-all-voters)
- [fetch_voters](#poll-fetch-voters)

### Methods

<a id="poll-end"></a>
#### `end`

```python
async end(self)
```

Ends the poll.

<a id="poll-fetch-all-voters"></a>
#### `fetch_all_voters`

```python
async fetch_all_voters(self) -> Dict[int, List[discohook.user.User]]
```

Fetch all the answers of the poll.
Returns
-------
Dict[:class:`int`, List[:class:`User`]]

<a id="poll-fetch-voters"></a>
#### `fetch_voters`

```python
async fetch_voters(self, answer_id: int, *, after: str | None = None, limit: int = 25) -> List[discohook.user.User]
```

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


<a id="class-pollanswer"></a>
## PollAnswer

`discohook.poll.PollAnswer`

An answer to a poll.
Properties
----------
answer_id: :class:`int`
The ID of the answer.
poll_media: Optional[:class:`PollMedia`]
The media of the answer.

### Method Index

- [new](#pollanswer-new)

### Methods

<a id="pollanswer-new"></a>
#### `new`

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


<a id="class-pollanswercount"></a>
## PollAnswerCount

`discohook.poll.PollAnswerCount`

Represents the count of an answer in a poll.
Properties
----------
answer_id: :class:`int`
The ID of the answer.
count: :class:`int`
The count of the answer.


<a id="class-pollmedia"></a>
## PollMedia

`discohook.poll.PollMedia`

The question of the poll. Only text is supported.
Properties
----------
text: Optional[:class:`str`]
The text of the media.
emoji: Optional[:class:`PartialEmoji`]
The emoji of the media.

