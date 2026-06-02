---
title: discohook.resolver
---

# `discohook.resolver`

## Functions

- [build_context_menu_param](#build-context-menu-param)
- [build_modal_params](#build-modal-params)
- [build_slash_command_params](#build-slash-command-params)
- [handle_params_by_signature](#handle-params-by-signature)
- [parse_generic_options](#parse-generic-options)
- [resolve_select_menu_values](#resolve-select-menu-values)

<a id="build-context-menu-param"></a>
## `build_context_menu_param`

**Qualified Name:** `discohook.resolver.build_context_menu_param`

### Signature

```python
build_context_menu_param(interaction: discohook.interaction.Interaction)
```


<a id="build-modal-params"></a>
## `build_modal_params`

**Qualified Name:** `discohook.resolver.build_modal_params`

### Signature

```python
build_modal_params(func: Callable, interaction: discohook.interaction.Interaction)
```


<a id="build-slash-command-params"></a>
## `build_slash_command_params`

**Qualified Name:** `discohook.resolver.build_slash_command_params`

### Signature

```python
build_slash_command_params(func: Callable, interaction: discohook.interaction.Interaction, skips: int = 1)
```


<a id="handle-params-by-signature"></a>
## `handle_params_by_signature`

**Qualified Name:** `discohook.resolver.handle_params_by_signature`

### Signature

```python
handle_params_by_signature(func: Callable, options: Dict[str, Any], skips: int = 1) -> Tuple[List[Any], Dict[str, Any]]
```


<a id="parse-generic-options"></a>
## `parse_generic_options`

**Qualified Name:** `discohook.resolver.parse_generic_options`

### Signature

```python
parse_generic_options(payload: List[Dict[str, Any]], interaction: discohook.interaction.Interaction)
```


<a id="resolve-select-menu-values"></a>
## `resolve_select_menu_values`

**Qualified Name:** `discohook.resolver.resolve_select_menu_values`

### Signature

```python
resolve_select_menu_values(interaction: discohook.interaction.Interaction) -> List[Any]
```

