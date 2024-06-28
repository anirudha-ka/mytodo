"""This module provides the todo model-controller."""

from typing import Any, Dict, NamedTuple

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int