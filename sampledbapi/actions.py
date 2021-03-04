"""
This is the module docstring.
"""

from typing import List

from sampledbapi import SampleDBObject, getData

__all__ = ["Action", "getList", "get"]


class Action(SampleDBObject):

    action_id: int = None
    instrument_id: int = None
    type: str = None
    type_id: int = None
    name: str = None
    description: str = None
    is_hidden: bool = None
    schema: dict = None


def getList() -> List[Action]:
    """Get a list of all actions.

    Returns:
        List: List of :class:`~sampledbapi.actions.Action` objects.
    """
    return [Action(a) for a in getData("actions")]


def get(action_id: int) -> Action:
    """Get the specific action (action_id).

    Args:
        action_id (int): ID of the action to be retrieved.

    Returns:
        Action: The requested :class:`~sampledbapi.action.Action`.
    """
    if isinstance(action_id, int):
        return Action(getData("actions/{}".format(action_id)))
    else:
        raise TypeError()
