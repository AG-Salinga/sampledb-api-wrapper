from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get", "getVersion", "getPublic",
           "getAllUsersPermissions", "getUserPermissions",
           "getAllGroupsPermissions", "getGroupPermissions",
           "getAllProjectsPermissions", "getProjectPermissions",
           "getLocationList", "getLocation", "getFileList", "getFileInfo"]


def getList() -> List:
    """Get a list of all objects visible to the current user.

    The list only contains the current version of each object. By passing the
    parameter q to the query, the Advanced Search can be used. By passing the
    parameters action_id or action_type objects can be filtered by the action
    they were created with or by their type (e.g. sample or measurement).
    """
    return getData("objects")


def get(object_id: int) -> Dict:
    """Get the current version of an object (object_id)."""
    if isinstance(object_id, int):
        return getData("objects/{}".format(object_id))
    else:
        raise TypeError()


def getVersion(object_id: int, version_id: int) -> Dict:
    """Get the specific version (version_id) of an object (object_id)."""
    if isinstance(object_id, int) and isinstance(version_id, int):
        return getData(
            "objects/{}/versions/{}" % (object_id, version_id)
        )
    else:
        raise TypeError()


"""Permissions"""


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


"""Locations"""


def getLocationList(object_id: int) -> List:
    """Get a list of all object locations assignments for a specific object (object_id)."""
    if isinstance(object_id, int):
        return getData("objects/{}/locations".format(object_id))
    else:
        raise TypeError()


def getLocation(object_id: int, location_id: int) -> Dict:
    """Get a specific object location assignment (location_id) for a specific object (object_id)."""
    if isinstance(object_id, int) and isinstance(location_id, int):
        return getData(
            "objects/{}/locations/{}" % (object_id, location_id)
        )
    else:
        raise TypeError()


"""Files"""


def getFileList(object_id: int) -> List:
    """Get a list of all files for a specific object (object_id)."""
    if isinstance(object_id, int):
        return getData("objects/{}/files".format(object_id))
    else:
        raise TypeError()


def getFileInfo(object_id: int, file_id: int) -> Dict:
    """Get a specific file (file_id) for a specific object (object_id)."""
    if isinstance(object_id, int) and isinstance(file_id, int):
        return getData(
            "objects/{}/files/{}" % (object_id, file_id)
        )
    else:
        raise TypeError()
