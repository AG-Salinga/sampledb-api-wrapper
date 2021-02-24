"""
This is the module docstring.
"""

from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList(object_id: int) -> List:
    """Get a list of all comments for a specific object (object_id)."""
    if isinstance(object_id, int):
        return getData("{}/comments".format(object_id))
    else:
        raise TypeError()


def get(object_id: int, comment_id: int) -> Dict:
    """Get specific comment (comment_id) for a specific object (object_id)."""
    if isinstance(object_id, int) and isinstance(comment_id, int):
        return getData("{}/comments/{}".format(object_id, comment_id))
    else:
        raise TypeError()
