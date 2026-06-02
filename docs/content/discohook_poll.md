---
title: discohook.poll
---

# `discohook.poll`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/poll.py`

## Classes

- [Poll](#class-poll)
- [PollAnswer](#class-pollanswer)
- [PollAnswerCount](#class-pollanswercount)
- [PollMedia](#class-pollmedia)

## Class `Poll`

A poll object.

### Properties

- **question** (`Optional[:class:`str`]`)
    The question of the poll.
- **answers** (`Optional[List[:class:`PollAnswer`]]`)
    The answers to the poll.
- **expiry** (`Optional[:class:`int`]`)
    The expiry time of the poll.
- **allow_multiselect** (`:class:`bool``)
    Whether the poll allows multiple answers.
- **layout** (`:class:`PollLayoutType``)
    The layout of the poll.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/poll.py`
- Line: `120`

### Methods

#### `end`

```python
end(self)
```

Ends the poll.

#### `fetch_all_voters`

```python
fetch_all_voters(self) -> Dict[int, List[discohook.user.User]]
```

Fetch all the answers of the poll.
### Returns

Dict[:class:`int`, List[:class:`User`]]

#### `fetch_voters`

```python
fetch_voters(self, answer_id: int, *, after: str | None = None, limit: int = 25) -> List[discohook.user.User]
```

Fetch the voters of an answer with pagination.
### Parameters

- **answer_id** (`:class:`int``)
    The ID of the answer.
- **after** (`Optional[:class:`str`]`)
    The ID of the last user fetched.
- **limit** (`:class:`int``)
    The number of users to fetch. Maximum is 100.

### Returns

List[:class:`User`]

#### `new`

```python
new(question: str, *answers: discohook.poll.PollAnswer, expiry: int | None = None, allow_multiselect: bool = False, layout: int = <PollLayoutType.default: 1>) -> 'Poll'
```

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `PollAnswer`

An answer to a poll.

### Properties

- **answer_id** (`:class:`int``)
    The ID of the answer.
- **poll_media** (`Optional[:class:`PollMedia`]`)
    The media of the answer.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/poll.py`
- Line: `44`

### Methods

#### `new`

```python
new(answer_id: int, media: str | discohook.poll.PollMedia) -> 'PollAnswer'
```

Create a new poll answer.
### Parameters

- **answer_id** (`:class:`int``)
    The ID of the answer.
- **media** (`Union[:class:`str`, :class:`PollMedia`]`)
    The media of the answer.

### Returns

:class:`PollAnswer`
    The newly created poll answer.

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```


## Class `PollAnswerCount`

Represents the count of an answer in a poll.

### Properties

- **answer_id** (`:class:`int``)
    The ID of the answer.
- **count** (`:class:`int``)
    The count of the answer.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/poll.py`
- Line: `93`

### Methods

#### `me_voted`

```python
me_voted(self) -> bool
```


## Class `PollMedia`

The question of the poll. Only text is supported.

### Properties

- **text** (`Optional[:class:`str`]`)
    The text of the media.
- **emoji** (`Optional[:class:`PartialEmoji`]`)
    The emoji of the media.

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/poll.py`
- Line: `13`

### Methods

#### `from_str`

```python
from_str(text: str) -> 'PollMedia'
```

#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

