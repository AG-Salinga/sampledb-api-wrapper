"""
This is the module docstring.
"""

from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList() -> List:
    """Get a list of all actions."""
    return getData("actions")


def get(action_id: int) -> Dict:
    """Get the specific action (action_id)."""
    if isinstance(action_id, int):
        return getData("actions/{}".format(action_id))
    else:
        raise TypeError()
