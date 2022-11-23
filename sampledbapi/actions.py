"""
This is the module docstring.
"""

from typing import List, Optional

from sampledbapi import SampleDBObject, get_data

__all__ = ["Action", "get_list", "get"]


class Action(SampleDBObject):

    action_id: Optional[int] = None
    instrument_id: Optional[int] = None
    type: Optional[str] = None
    type_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_hidden: Optional[bool] = None
    schema: Optional[dict] = None

    def __repr__(self) -> str:
        return f"Action {self.action_id} ({self.name})"


def get_list() -> List[Action]:
    """Get a list of all actions.

    Returns:
        List: List of :class:`~sampledbapi.actions.Action` objects.
    """
    return [Action(a) for a in get_data("actions")]


def get(action_id: int) -> Action:
    """Get the specific action (action_id).

    Args:
        action_id (int): ID of the action to be retrieved.

    Returns:
        Action: The requested :class:`~sampledbapi.action.Action`.
    """
    if isinstance(action_id, int):
        return Action(get_data(f"actions/{action_id}"))
    else:
        raise TypeError()
