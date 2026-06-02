---
title: discohook.enums
---

# `discohook.enums`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`

## Classes

- [AllowedMentionsType](#class-allowedmentionstype)
- [ApplicationCommandOptionType](#class-applicationcommandoptiontype)
- [ApplicationCommandType](#class-applicationcommandtype)
- [ApplicationIntegrationType](#class-applicationintegrationtype)
- [ButtonStyle](#class-buttonstyle)
- [ChannelType](#class-channeltype)
- [ComponentType](#class-componenttype)
- [InteractionCallbackType](#class-interactioncallbacktype)
- [InteractionContextType](#class-interactioncontexttype)
- [InteractionType](#class-interactiontype)
- [ModalFieldType](#class-modalfieldtype)
- [PollLayoutType](#class-polllayouttype)
- [SelectDefaultValueType](#class-selectdefaultvaluetype)
- [SelectType](#class-selecttype)
- [TextInputFieldLength](#class-textinputfieldlength)
- [WebhookType](#class-webhooktype)

## Class `AllowedMentionsType`

The type of mentions allowed in a message.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.str`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `260`

### Methods

#### `capitalize`

```python
capitalize(self, /)
```

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

#### `casefold`

```python
casefold(self, /)
```

Return a version of the string suitable for caseless comparisons.

#### `center`

```python
center(self, width, fillchar=' ', /)
```

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

#### `count`

Return the number of non-overlapping occurrences of substring sub in string S[start:end].

Optional arguments start and end are interpreted as in slice notation.

#### `encode`

```python
encode(self, /, encoding='utf-8', errors='strict')
```

Encode the string using the codec registered for encoding.

encoding
  The encoding in which to encode the string.
errors
  The error handling scheme to use for encoding errors.
  The default is 'strict' meaning that encoding errors raise a
  UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
  'xmlcharrefreplace' as well as any other name registered with
  codecs.register_error that can handle UnicodeEncodeErrors.

#### `endswith`

Return True if the string ends with the specified suffix, False otherwise.

suffix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.

#### `expandtabs`

```python
expandtabs(self, /, tabsize=8)
```

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

#### `find`

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Return -1 on failure.

#### `format`

```python
format(self, /, *args, **kwargs)
```

Return a formatted version of the string, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').

#### `format_map`

```python
format_map(self, mapping, /)
```

Return a formatted version of the string, using substitutions from mapping.
The substitutions are identified by braces ('{' and '}').

#### `index`

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Raises ValueError when the substring is not found.

#### `isalnum`

```python
isalnum(self, /)
```

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

#### `isalpha`

```python
isalpha(self, /)
```

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

#### `isascii`

```python
isascii(self, /)
```

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

#### `isdecimal`

```python
isdecimal(self, /)
```

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

#### `isdigit`

```python
isdigit(self, /)
```

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

#### `isidentifier`

```python
isidentifier(self, /)
```

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as "def" or "class".

#### `islower`

```python
islower(self, /)
```

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

#### `isnumeric`

```python
isnumeric(self, /)
```

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

#### `isprintable`

```python
isprintable(self, /)
```

Return True if all characters in the string are printable, False otherwise.

A character is printable if repr() may use it in its output.

#### `isspace`

```python
isspace(self, /)
```

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

#### `istitle`

```python
istitle(self, /)
```

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

#### `isupper`

```python
isupper(self, /)
```

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

#### `join`

```python
join(self, iterable, /)
```

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

- **Example** (`'.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'`)

#### `ljust`

```python
ljust(self, width, fillchar=' ', /)
```

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

#### `lower`

```python
lower(self, /)
```

Return a copy of the string converted to lowercase.

#### `lstrip`

```python
lstrip(self, chars=None, /)
```

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

#### `partition`

```python
partition(self, sep, /)
```

Partition the string into three parts using the given separator.

This will search for the separator in the string.  If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

#### `removeprefix`

```python
removeprefix(self, prefix, /)
```

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

#### `removesuffix`

```python
removesuffix(self, suffix, /)
```

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

#### `replace`

```python
replace(self, old, new, /, count=-1)
```

Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

#### `rfind`

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Return -1 on failure.

#### `rindex`

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Raises ValueError when the substring is not found.

#### `rjust`

```python
rjust(self, width, fillchar=' ', /)
```

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

#### `rpartition`

```python
rpartition(self, sep, /)
```

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

#### `rsplit`

```python
rsplit(self, /, sep=None, maxsplit=-1)
```

Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \n \r \t \f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

#### `rstrip`

```python
rstrip(self, chars=None, /)
```

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

#### `split`

```python
split(self, /, sep=None, maxsplit=-1)
```

Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \n \r \t \f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally
delimited.  With natural text that includes punctuation, consider using
the regular expression module.

#### `splitlines`

```python
splitlines(self, /, keepends=False)
```

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

#### `startswith`

Return True if the string starts with the specified prefix, False otherwise.

prefix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.

#### `strip`

```python
strip(self, chars=None, /)
```

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

#### `swapcase`

```python
swapcase(self, /)
```

Convert uppercase characters to lowercase and lowercase characters to uppercase.

#### `title`

```python
title(self, /)
```

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

#### `translate`

```python
translate(self, table, /)
```

Replace each character in the string using the given translation table.

  table
    Translation table, which must be a mapping of Unicode ordinals to
    Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list.  If this operation raises LookupError, the character is
left untouched.  Characters mapped to None are deleted.

#### `upper`

```python
upper(self, /)
```

Return a copy of the string converted to uppercase.

#### `zfill`

```python
zfill(self, width, /)
```

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.


## Class `ApplicationCommandOptionType`

The type of application command option.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `81`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `ApplicationCommandType`

The type of application command.

### Attributes

- **slash** (`:class:`int``)
    Used to specify a slash command.
- **user** (`:class:`int``)
    Used to specify a user command.
- **message** (`:class:`int``)
    Used to specify a message command.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `61`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `ApplicationIntegrationType`

Installation context(s) where the command is available.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `294`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `ButtonStyle`

Represents the style of a button.

### Attributes

- **blurple** (`:class:`int``)
    Used to specify a blurple button.
- **grey** (`:class:`int``)
    Used to specify a grey button.
- **green** (`:class:`int``)
    Used to specify a green button.
- **red** (`:class:`int``)
    Used to specify a red button.
- **link** (`:class:`int``)
    Used to specify a link type button.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `223`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `ChannelType`

Use to specify discord channel type in application command Option.

### Attributes

- **guild_text** (`:class:`int``)
    Used to specify a guild text channel.
- **dm** (`:class:`int``)
    Used to specify a dm channel.
- **guild_voice** (`:class:`int``)
    Used to specify a guild voice channel.
- **group_dm** (`:class:`int``)
    Used to specify a group dm channel.
- **guild_category** (`:class:`int``)
    Used to specify a guild category channel.
- **guild_announcement** (`:class:`int``)
    Used to specify a guild announcement channel.
- **guild_announcement_thread** (`:class:`int``)
    Used to specify a guild announcement thread channel.
- **public_thread** (`:class:`int``)
    Used to specify a guild public thread channel.
- **private_thread** (`:class:`int``)
    Used to specify a guild private thread channel.
- **guild_stage_voice** (`:class:`int``)
    Used to specify a guild stage voice channel.
- **guild_directory** (`:class:`int``)
    Used to specify a guild directory channel.
- **guild_forum** (`:class:`int``)
    Used to specify a guild forum channel.
- **guild_media** (`:class:`int``)
    Used to specify a guild media channel.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `101`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `ComponentType`

The type of message component.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `182`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `InteractionCallbackType`

The type of interaction callback.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `164`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `InteractionContextType`

The type of interaction context.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `284`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `InteractionType`

The type of interaction received from discord.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `150`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `ModalFieldType`

The type of field in a modal.

Used internally by the library. You should not need to use this.

### Attributes

- **text_input** (`:class:`int``)
    Used to specify a text input field.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `46`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `PollLayoutType`

The type of layout for a poll.

### Attributes

- **default** (`:class:`int``)
    Used to specify the default layout.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `303`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `SelectDefaultValueType`

The type of default value for a select menu.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.str`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `272`

### Methods

#### `capitalize`

```python
capitalize(self, /)
```

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

#### `casefold`

```python
casefold(self, /)
```

Return a version of the string suitable for caseless comparisons.

#### `center`

```python
center(self, width, fillchar=' ', /)
```

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

#### `count`

Return the number of non-overlapping occurrences of substring sub in string S[start:end].

Optional arguments start and end are interpreted as in slice notation.

#### `encode`

```python
encode(self, /, encoding='utf-8', errors='strict')
```

Encode the string using the codec registered for encoding.

encoding
  The encoding in which to encode the string.
errors
  The error handling scheme to use for encoding errors.
  The default is 'strict' meaning that encoding errors raise a
  UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
  'xmlcharrefreplace' as well as any other name registered with
  codecs.register_error that can handle UnicodeEncodeErrors.

#### `endswith`

Return True if the string ends with the specified suffix, False otherwise.

suffix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.

#### `expandtabs`

```python
expandtabs(self, /, tabsize=8)
```

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

#### `find`

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Return -1 on failure.

#### `format`

```python
format(self, /, *args, **kwargs)
```

Return a formatted version of the string, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').

#### `format_map`

```python
format_map(self, mapping, /)
```

Return a formatted version of the string, using substitutions from mapping.
The substitutions are identified by braces ('{' and '}').

#### `index`

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Raises ValueError when the substring is not found.

#### `isalnum`

```python
isalnum(self, /)
```

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

#### `isalpha`

```python
isalpha(self, /)
```

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

#### `isascii`

```python
isascii(self, /)
```

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

#### `isdecimal`

```python
isdecimal(self, /)
```

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

#### `isdigit`

```python
isdigit(self, /)
```

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

#### `isidentifier`

```python
isidentifier(self, /)
```

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as "def" or "class".

#### `islower`

```python
islower(self, /)
```

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

#### `isnumeric`

```python
isnumeric(self, /)
```

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

#### `isprintable`

```python
isprintable(self, /)
```

Return True if all characters in the string are printable, False otherwise.

A character is printable if repr() may use it in its output.

#### `isspace`

```python
isspace(self, /)
```

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

#### `istitle`

```python
istitle(self, /)
```

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

#### `isupper`

```python
isupper(self, /)
```

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

#### `join`

```python
join(self, iterable, /)
```

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

- **Example** (`'.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'`)

#### `ljust`

```python
ljust(self, width, fillchar=' ', /)
```

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

#### `lower`

```python
lower(self, /)
```

Return a copy of the string converted to lowercase.

#### `lstrip`

```python
lstrip(self, chars=None, /)
```

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

#### `partition`

```python
partition(self, sep, /)
```

Partition the string into three parts using the given separator.

This will search for the separator in the string.  If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

#### `removeprefix`

```python
removeprefix(self, prefix, /)
```

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

#### `removesuffix`

```python
removesuffix(self, suffix, /)
```

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

#### `replace`

```python
replace(self, old, new, /, count=-1)
```

Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

#### `rfind`

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Return -1 on failure.

#### `rindex`

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation.
Raises ValueError when the substring is not found.

#### `rjust`

```python
rjust(self, width, fillchar=' ', /)
```

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

#### `rpartition`

```python
rpartition(self, sep, /)
```

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

#### `rsplit`

```python
rsplit(self, /, sep=None, maxsplit=-1)
```

Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \n \r \t \f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

#### `rstrip`

```python
rstrip(self, chars=None, /)
```

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

#### `split`

```python
split(self, /, sep=None, maxsplit=-1)
```

Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \n \r \t \f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally
delimited.  With natural text that includes punctuation, consider using
the regular expression module.

#### `splitlines`

```python
splitlines(self, /, keepends=False)
```

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

#### `startswith`

Return True if the string starts with the specified prefix, False otherwise.

prefix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.

#### `strip`

```python
strip(self, chars=None, /)
```

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

#### `swapcase`

```python
swapcase(self, /)
```

Convert uppercase characters to lowercase and lowercase characters to uppercase.

#### `title`

```python
title(self, /)
```

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

#### `translate`

```python
translate(self, table, /)
```

Replace each character in the string using the given translation table.

  table
    Translation table, which must be a mapping of Unicode ordinals to
    Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list.  If this operation raises LookupError, the character is
left untouched.  Characters mapped to None are deleted.

#### `upper`

```python
upper(self, /)
```

Return a copy of the string converted to uppercase.

#### `zfill`

```python
zfill(self, width, /)
```

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.


## Class `SelectType`

The type of select menu.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `211`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `TextInputFieldLength`

The length of a text input field for a modal.

### Attributes

- **short** (`:class:`int``)
    Used to specify a short length text input field (up to 100 characters).
- **long** (`:class:`int``)
    Used to specify a long length text input field (up to 3000 characters).

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `30`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Class `WebhookType`

The type of webhook.

Used internally by the library. You should not need to use this.

### Inheritance

- `builtins.int`
- `enum.Enum`

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `248`

### Methods

#### `as_integer_ratio`

```python
as_integer_ratio(self, /)
```

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

#### `bit_count`

```python
bit_count(self, /)
```

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

>>> bin(13)
'0b1101'
>>> (13).bit_count()
3

#### `bit_length`

```python
bit_length(self, /)
```

Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

#### `conjugate`

```python
conjugate(self, /)
```

Returns self, the complex conjugate of any int.

#### `is_integer`

```python
is_integer(self, /)
```

Returns True. Exists for duck type compatibility with float.is_integer.

#### `to_bytes`

```python
to_bytes(self, /, length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  sys.byteorder as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.


## Functions

- [try_enum](#try-enum)

## `try_enum`

### Signature

```python
try_enum(enum_class, value)
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/enums.py`
- Line: `23`

