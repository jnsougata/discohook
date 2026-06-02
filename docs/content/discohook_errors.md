---
title: discohook.errors
---

# `discohook.errors`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/errors.py`

## Classes

- [CheckFailure](#class-checkfailure)
- [HTTPException](#class-httpexception)
- [InteractionTypeMismatch](#class-interactiontypemismatch)
- [RateLimitExceeded](#class-ratelimitexceeded)
- [UnknownInteractionType](#class-unknowninteractiontype)

## Class `CheckFailure`

Raised when a check fails.

### Inheritance

- `builtins.Exception`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/errors.py`
- Line: `15`

### Methods

#### `add_note`

```python
add_note(self, note, /)
```

Add a note to the exception

#### `with_traceback`

```python
with_traceback(self, tb, /)
```

Set self.__traceback__ to tb and return self.


## Class `HTTPException`

Raised when an HTTP request operation fails.

### Inheritance

- `builtins.Exception`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/errors.py`
- Line: `29`

### Methods

#### `add_note`

```python
add_note(self, note, /)
```

Add a note to the exception

#### `with_traceback`

```python
with_traceback(self, tb, /)
```

Set self.__traceback__ to tb and return self.


## Class `InteractionTypeMismatch`

Raised when the interaction type is not the expected type.

### Inheritance

- `builtins.Exception`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/errors.py`
- Line: `8`

### Methods

#### `add_note`

```python
add_note(self, note, /)
```

Add a note to the exception

#### `with_traceback`

```python
with_traceback(self, tb, /)
```

Set self.__traceback__ to tb and return self.


## Class `RateLimitExceeded`

Raised when a rate limit is exceeded.

### Inheritance

- `builtins.Exception`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/errors.py`
- Line: `44`

### Methods

#### `add_note`

```python
add_note(self, note, /)
```

Add a note to the exception

#### `with_traceback`

```python
with_traceback(self, tb, /)
```

Set self.__traceback__ to tb and return self.


## Class `UnknownInteractionType`

Raised when the interaction type is unknown.

### Inheritance

- `builtins.Exception`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/errors.py`
- Line: `22`

### Methods

#### `add_note`

```python
add_note(self, note, /)
```

Add a note to the exception

#### `with_traceback`

```python
with_traceback(self, tb, /)
```

Set self.__traceback__ to tb and return self.

