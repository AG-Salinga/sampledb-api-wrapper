from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get", "getCurrent"]


def getList() -> List:
    """Get a list of all users.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#users>`_
    """
    return getData("users")


def get(user_id: int) -> Dict:
    """Get the specific user (user_id).

    Args:
        user_id (int): ID of the user to be retrieved.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#users>`_
    """
    if isinstance(user_id, int):
        return getData("users/{}".format(user_id))
    else:
        raise TypeError()


def getCurrent() -> Dict:
    """Get the current user.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#actions>`_
    """
    return getData("users/me")
