from typing import List, Optional

from sampledbapi import SampleDBObject, get_data

__all__ = ["User", "get_list", "get", "get_current"]


class User(SampleDBObject):

    user_id: Optional[int] = None
    name: Optional[str] = None
    orcid: Optional[str] = None
    affiliation: Optional[str] = None

    def __repr__(self) -> str:
        return f"User {self.user_id} ({self.name})"


def get_list() -> List[User]:
    """Get a list of all users.

    Returns:
        List: List of :class:`~sampledbapi.users.User` objects.
    """
    return [User(d) for d in get_data("users")]


def get(user_id: int) -> User:
    """Get the specific user (user_id).

    Args:
        user_id (int): ID of the user to be retrieved.

    Returns:
        User: Requested :class:`~sampledbapi.users.User`.
    """
    if isinstance(user_id, int):
        return User(get_data(f"users/{user_id}"))
    else:
        raise TypeError()


def get_current() -> User:
    """Get the current user.

    Returns:
        User: Current :class:`~sampledbapi.users.User`.
    """
    return User(get_data("users/me"))
