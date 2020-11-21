from typing import Dict, List

from sampledbapi import getData


def getPublic(object_id: int) -> bool:
    """Get whether or not an object is public."""

    if isinstance(object_id, int):
        return getData("objects/{}/permissions/public".format(object_id))
    else:
        raise TypeError()


def getAllUsersPermissions(object_id: int) -> Dict:
    """Get a mapping of user IDs to their permissions."""

    if isinstance(object_id, int):
        return getData("objects/{}/permissions/users".format(object_id))
    else:
        raise TypeError()


def getUserPermissions(object_id: int, user_id: int) -> str:
    """Get the permissions of a user for an object."""

    if isinstance(object_id, int) and isinstance(user_id, int):
        return getData(
            "objects/{}/permissions/users/{}" % (object_id, user_id)
        )
    else:
        raise TypeError()


def getAllGroupsPermissions(object_id: int) -> Dict:
    """Get a mapping of group IDs to their permissions."""

    if isinstance(object_id, int):
        return getData("objects/{}/permissions/groups".format(object_id))
    else:
        raise TypeError()


def getGroupPermissions(object_id: int, group_id: int) -> str:
    """Get the permissions of a group for an object."""

    if isinstance(object_id, int) and isinstance(group_id, int):
        return getData(
            "objects/{}/permissions/groups/{}" % (object_id, group_id)
        )
    else:
        raise TypeError()


def getAllProjectsPermissions(object_id: int) -> Dict:
    """Get a mapping of group IDs to their permissions."""

    if isinstance(object_id, int):
        return getData("objects/{}/permissions/projects".format(object_id))
    else:
        raise TypeError()


def getProjectPermissions(object_id: int, project_id: int) -> str:
    """Get the permissions of a group for an object."""

    if isinstance(object_id, int) and isinstance(project_id, int):
        return getData(
            "objects/{}/permissions/projects/{}" % (object_id, project_id)
        )
    else:
        raise TypeError()
