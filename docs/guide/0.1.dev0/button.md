---
title: discohook.button
---

# `discohook.button`

## Classes

- [Button](#class-button)

<a id="class-button"></a>
## Button

`discohook.button.Button`

Represents a discord button type component.
#### _Attributes_

- _**label** (`str`): Label of the button._
- _**url** (`str | None`): Url to be opened for `ButtonStyle.link`._
- _**style** (`ButtonStyle`): Style of the button._
- _**disabled** (`bool`): Whether the button is disabled or not._
- _**emoji** (`PartialEmoji`): Emoji object for the button._
- _**handler** (`Handler`): Handler for the button._

### Method Index

- [to_dict](#button-to-dict)

### Methods

<a id="button-to-dict"></a>
#### `to_dict`

```python
to_dict(self) -> Dict[str, Any]
```

Builds a dictionary representation of the button.
This is used internally by the library. It is rarely required for general purpose use cases.
#### _Returns_

- **Type:** `dict`
  - Dictionary representation of the button.

