from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList() -> List:
    """Get a list of all action types.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#action-types>`_
    """
    return getData("action_types")


def get(type_id: int) -> Dict:
    """Get the specific action type (type_id).

    Args:
        type_id (int): ID of the action type.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#action-types>`_
    """
    if isinstance(type_id, int):
        return getData("actions/{}".format(type_id))
    else:
        raise TypeError()
