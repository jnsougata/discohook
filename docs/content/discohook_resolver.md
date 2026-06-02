---
title: discohook.resolver
---

# `discohook.resolver`

## Module Information

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`

## Functions

- [build_context_menu_param](#build-context-menu-param)
- [build_modal_params](#build-modal-params)
- [build_slash_command_params](#build-slash-command-params)
- [handle_params_by_signature](#handle-params-by-signature)
- [parse_generic_options](#parse-generic-options)
- [resolve_select_menu_values](#resolve-select-menu-values)

## `build_context_menu_param`

### Signature

```python
build_context_menu_param(interaction: discohook.interaction.Interaction)
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`
- Line: `117`


## `build_modal_params`

### Signature

```python
build_modal_params(func: Callable, interaction: discohook.interaction.Interaction)
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`
- Line: `176`


## `build_slash_command_params`

### Signature

```python
build_slash_command_params(func: Callable, interaction: discohook.interaction.Interaction, skips: int = 1)
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`
- Line: `103`


## `handle_params_by_signature`

### Signature

```python
handle_params_by_signature(func: Callable, options: Dict[str, Any], skips: int = 1) -> Tuple[List[Any], Dict[str, Any]]
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`
- Line: `16`


## `parse_generic_options`

### Signature

```python
parse_generic_options(payload: List[Dict[str, Any]], interaction: discohook.interaction.Interaction)
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`
- Line: `49`


## `resolve_select_menu_values`

### Signature

```python
resolve_select_menu_values(interaction: discohook.interaction.Interaction) -> List[Any]
```

### Source

- File: `/home/jnsougata/Projects/discohook/discohook/resolver.py`
- Line: `137`

