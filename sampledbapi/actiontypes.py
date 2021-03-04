from typing import List

from sampledbapi import SampleDBObject, getData
from sampledbapi.actions import Action

__all__ = ["ActionType", "getList", "get"]


class ActionType(SampleDBObject):

    type_id: int = None
    name: str = None
    object_name: str = None
    admin_only: bool = None


def getList() -> List[ActionType]:
    """Get a list of all action types.

    Returns:
        List: List of :class:`~sampledbapi.actiontypes.Actiontype` objects.
    """
    return [ActionType(a) for a in getData("action_types")]


def get(type_id: int) -> ActionType:
    """Get the specific action type (type_id).

    Args:
        type_id (int): ID of the action type.

    Returns:
        ActionType: The requested :class:`~sampledbapi.actiontypes.ActionType`.
    """
    if isinstance(type_id, int):
        return ActionType(getData("actions/{}".format(type_id)))
    else:
        raise TypeError()
