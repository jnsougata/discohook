from .enums import option_types
from typing import Optional, List, Dict, Any, Union, Callable


class Choice:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def to_json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value
        }


class Option:
    def __init__(self, name: str, description: str, required: bool = False):
        self.name = name
        self.description = description
        self.required = required


class StringOption(Option):
    def __init__(
            self,
            name: str,
            description: str,
            required: bool = False,
            max_length: int = 100,
            min_length: int = 1,
            choices: List[Choice] = None,
            auto_complete: bool = False,
    ):
        super().__init__(name, description, required)
        self.type = option_types.string.value

    def to_json(self) -> Dict[str, Any]:
        payload = {
            "name": self.name,
            "description": self.description,
        }
        if self.required:
            payload["required"] = self.required
        if self.choices:
            payload["choices"] = [choice.to_json() for choice in self.choices]
        if self.auto_complete:
            payload["autocomplete"] = self.auto_complete
        if self.max_length:
            payload["max_length"] = self.max_length
        if self.min_length:
            payload["min_length"] = self.min_length
        return payload
