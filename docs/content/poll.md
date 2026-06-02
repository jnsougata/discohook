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
## Class `Poll`

**Qualified Name:** `discohook.poll.Poll`

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

### Property Index

- [allow_multiselect](#poll-allow-multiselect)
- [answer_counts](#poll-answer-counts)
- [answers](#poll-answers)
- [expiry](#poll-expiry)
- [is_finalized](#poll-is-finalized)
- [layout](#poll-layout)
- [question](#poll-question)

### Method Index

- [end](#poll-end)
- [fetch_all_voters](#poll-fetch-all-voters)
- [fetch_voters](#poll-fetch-voters)
- [new](#poll-new)
- [to_dict](#poll-to-dict)

### Properties

<a id="poll-allow-multiselect"></a>
#### `allow_multiselect`

<a id="poll-answer-counts"></a>
#### `answer_counts`

<a id="poll-answers"></a>
#### `answers`

<a id="poll-expiry"></a>
#### `expiry`

<a id="poll-is-finalized"></a>
#### `is_finalized`

<a id="poll-layout"></a>
#### `layout`

<a id="poll-question"></a>
#### `question`

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

<a id="poll-new"></a>
#### `new`

<a id="poll-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-pollanswer"></a>
## Class `PollAnswer`

**Qualified Name:** `discohook.poll.PollAnswer`

An answer to a poll.

Properties
----------
answer_id: :class:`int`
The ID of the answer.
poll_media: Optional[:class:`PollMedia`]
The media of the answer.

### Property Index

- [id](#pollanswer-id)
- [media](#pollanswer-media)

### Method Index

- [new](#pollanswer-new)
- [to_dict](#pollanswer-to-dict)

### Properties

<a id="pollanswer-id"></a>
#### `id`

<a id="pollanswer-media"></a>
#### `media`

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

<a id="pollanswer-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


<a id="class-pollanswercount"></a>
## Class `PollAnswerCount`

**Qualified Name:** `discohook.poll.PollAnswerCount`

Represents the count of an answer in a poll.

Properties
----------
answer_id: :class:`int`
The ID of the answer.
count: :class:`int`
The count of the answer.

### Property Index

- [answer_id](#pollanswercount-answer-id)
- [count](#pollanswercount-count)

### Method Index

- [me_voted](#pollanswercount-me-voted)

### Properties

<a id="pollanswercount-answer-id"></a>
#### `answer_id`

<a id="pollanswercount-count"></a>
#### `count`

### Methods

<a id="pollanswercount-me-voted"></a>
#### `me_voted`

```python
me_voted(self) -> bool
```


<a id="class-pollmedia"></a>
## Class `PollMedia`

**Qualified Name:** `discohook.poll.PollMedia`

The question of the poll. Only text is supported.

Properties
----------
text: Optional[:class:`str`]
The text of the media.
emoji: Optional[:class:`PartialEmoji`]
The emoji of the media.

### Property Index

- [emoji](#pollmedia-emoji)
- [text](#pollmedia-text)

### Method Index

- [from_str](#pollmedia-from-str)
- [to_dict](#pollmedia-to-dict)

### Properties

<a id="pollmedia-emoji"></a>
#### `emoji`

<a id="pollmedia-text"></a>
#### `text`

### Methods

<a id="pollmedia-from-str"></a>
#### `from_str`

<a id="pollmedia-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

