from datetime import datetime, timedelta
from typing import List, Dict, Union, Any
try:
    from typing import TypedDict, NotRequired
except Exception:  # noqa
    from typing_extensions import TypedDict, NotRequired


def time_converter(time_value: Union[int, float, datetime]) -> float:
    if isinstance(time_value, datetime):
        return time_value.replace(microsecond=0).timestamp()
    else:
        return (datetime.now() + timedelta(seconds=time_value)).replace(microsecond=0).timestamp()


class Record(TypedDict, total=False):
    """
    Represents a record to be put into the base

    Parameters
    ----------
    key : str
        Key of the record
    expire_at : datetime
        Unix time at which the record will expire
    expire_after : int | float
        Time in seconds after which the record will expire
    """
    key: NotRequired[str]
    expire_at: NotRequired[datetime]
    expire_after: NotRequired[Union[int, float]]


class Updater:
    """
    Represents an updater to update a record in the base
    """
    def __init__(self) -> None:
        self._set = {}
        self._increment = {}
        self. _append = {}
        self._prepend = {}
        self._delete = []
    
    def set(self, field: str, value: Any):
        """
        Set a value to a field

        Parameters
        ----------
        field : str
            Field to be set
        value : Any
            Value to be set
        """
        self._set[field] = value
    
    def increment(self, field: str, value: Union[int, float] = 1):
        """
        Increment a field by a value (default: 1)

        Parameters
        ----------
        field : str
            Field to be incremented
        value : Union[int, float], optional
            Value to be incremented by, by default 1
        """
        self._increment[field] = value
    
    def append(self, field: str, value: List[Any]):
        """
        Append a value to a field (must be a list)

        Parameters
        ----------
        field : str
            Field to be appended to
        value : List[Any]
            Value to be appended
        """
        self._append[field] = value
    
    def prepend(self, field: str, value: List[Any]):
        """
        Prepend a value to a field (must be a list)

        Parameters
        ----------
        field : str
            Field to be prepended to
        value : List[Any]
            Value to be prepended
        """
        self._prepend[field] = value
    
    def delete(self, field: str):
        """
        Delete a field from the record

        Parameters
        ----------
        field : str
            Field to be deleted
        """
        self._delete.append(field)
    
    def json(self) -> Dict[str, Any]:
        payload = {}
        if self._set:
            payload["set"] = self._set
        if self._increment:
            payload["increment"] = self._increment
        if self._append:
            payload["append"] = self._append
        if self._prepend:
            payload["prepend"] = self._prepend
        if self._delete:
            payload["delete"] = self._delete
        return payload


class Query:
    """
    Represents a query to be used in the base
    """
    def __init__(self):
        self._payload = {}
    
    def equals(self, field: str, value: Any):
        """
        Works as equality operator in the query (==)
        """
        self._payload[field] = value
    
    def not_equals(self, field: str, value: Any):
        """
        Works as inequality operator in the query (!=)
        """
        self._payload[f"{field}?ne"] = value
    
    def greater_than(self, field: str, value: Any):
        """
        Works as greater than operator in the query (>)
        """
        self._payload[f"{field}?gt"] = value
    
    def greater_equal(self, field: str, value: Any):
        """
        Works as greater than or equal to operator in the query (>=)
        """
        self._payload[f"{field}?gte"] = value
    
    def less_than(self, field: str, value: Any):
        """
        Works as less than operator in the query (<)
        """
        self._payload[f"{field}?lt"] = value
    
    def less_equal(self, field: str, value: Any):
        """
        Works as less than or equal to operator in the query (<=)
        """
        self._payload[f"{field}?lte"] = value
    
    def contains(self, field: str, value: Any):
        """
        Works as contains operator in the query (in)
        """
        self._payload[f"{field}?contains"] = value
    
    def not_contains(self, field: str, value: Any):
        """
        Works as not contains operator in the query (not in)
        """
        self._payload[f"{field}?not_contains"] = value
    
    def range(self, field: str, start: Union[int, float], end: Union[int, float]):
        """
        Works as range operator in the query (range(start, end))
        """
        self._payload[f"{field}?r"] = [start, end]
    
    def prefix(self, field: str, value: str):
        """
        Works as prefix operator in the query (startswith)
        """
        self._payload[f"{field}?pfx"] = value

    def json(self) -> Dict[str, Any]:
        return self._payload
