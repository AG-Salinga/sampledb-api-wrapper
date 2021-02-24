"""
This is the module docstring.
"""

from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList() -> List:
    """Get a list of all actions.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#actions>`_
    """
    return getData("actions")


def get(action_id: int) -> Dict:
    """Get the specific action (action_id).

    Args:
        action_id (int): ID of the action to be retrieved.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#actions>`_
    """
    if isinstance(action_id, int):
        return getData("actions/{}".format(action_id))
    else:
        raise TypeError()
