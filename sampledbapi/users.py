from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get", "getCurrent"]


def getList() -> List:
    """Get a list of all users."""
    return getData("users")


def get(user_id: int) -> Dict:
    """Get the specific user (user_id)."""
    if isinstance(user_id, int):
        return getData("users/{}".format(user_id))
    else:
        raise TypeError()


def getCurrent() -> Dict:
    """Get the current user."""
    return getData("users/me")
