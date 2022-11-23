from typing import List, Optional

from sampledbapi import SampleDBObject, get_data

__all__ = ["ActionType", "get_list", "get"]


class ActionType(SampleDBObject):

    type_id: Optional[int] = None
    name: Optional[str] = None
    object_name: Optional[str] = None
    admin_only: Optional[bool] = None

    def __repr__(self) -> str:
        return f"ActionType {self.type_id} ({self.name})"


def get_list() -> List[ActionType]:
    """Get a list of all action types.

    Returns:
        List: List of :class:`~sampledbapi.actiontypes.Actiontype` objects.
    """
    return [ActionType(a) for a in get_data("action_types")]


def get(type_id: int) -> ActionType:
    """Get the specific action type (type_id).

    Args:
        type_id (int): ID of the action type.

    Returns:
        ActionType: The requested :class:`~sampledbapi.actiontypes.ActionType`.
    """
    if isinstance(type_id, int):
        return ActionType(get_data(f"action_types/{type_id}"))
    else:
        raise TypeError()
