from typing import List

from sampledbapi import SampleDBObject, getData

__all__ = ["User", "getList", "get", "getCurrent"]


class User(SampleDBObject):

    user_id: int = None
    name: str = None
    orcid: str = None
    affiliation: str = None


def getList() -> List[User]:
    """Get a list of all users.

    Returns:
        List: List of :class:`~sampledbapi.users.User` objects.
    """
    return [User(d) for d in getData("users")]


def get(user_id: int) -> User:
    """Get the specific user (user_id).

    Args:
        user_id (int): ID of the user to be retrieved.

    Returns:
        User: Requested :class:`~sampledbapi.users.User`.
    """
    if isinstance(user_id, int):
        return User(getData("users/{}".format(user_id)))
    else:
        raise TypeError()


def getCurrent() -> User:
    """Get the current user.

    Returns:
        User: Current :class:`~sampledbapi.users.User`.
    """
    return User(getData("users/me"))
