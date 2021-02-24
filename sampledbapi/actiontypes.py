from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList() -> List:
    """Get a list of all action types."""
    return getData("action_types")


def get(type_id: int) -> Dict:
    """Get the specific action type (type_id)."""
    if isinstance(type_id, int):
        return getData("actions/{}".format(type_id))
    else:
        raise TypeError()
