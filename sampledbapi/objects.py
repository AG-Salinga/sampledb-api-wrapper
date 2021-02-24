import base64
import os
from io import IOBase
from typing import BinaryIO, Dict, List

from requests import Response

from sampledbapi import getData, postData, putData

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


def setPublic(object_id: int, public: bool) -> Response:
    """Set whether or not an object is public."""
    if isinstance(object_id, int) and isinstance(public, bool):
        return putData("objects/{}/permissions/public".format(object_id),
                       public)
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
            "objects/{}/permissions/users/{}".format(object_id, user_id)
        )
    else:
        raise TypeError()


def setUserPermissions(object_id: int, user_id: int,
                       permissions: str) -> Response:
    """Set the permissions of a user for an object."""
    if (isinstance(object_id, int) and isinstance(user_id, int) and
            isinstance(permissions, str)):
        return putData(
            "objects/{}/permissions/users/{}".format(object_id, user_id),
            permissions
        )
    else:
        raise TypeError()


def getAllGroupsPermissions(object_id: int) -> Dict:
    """Get a mapping of basic group IDs to their permissions."""
    if isinstance(object_id, int):
        return getData("objects/{}/permissions/groups".format(object_id))
    else:
        raise TypeError()


def getGroupPermissions(object_id: int, group_id: int) -> str:
    """Get the permissions of a basic group for an object."""
    if isinstance(object_id, int) and isinstance(group_id, int):
        return getData(
            "objects/{}/permissions/groups/{}" % (object_id, group_id)
        )
    else:
        raise TypeError()


def setGroupPermissions(object_id: int, group_id: int,
                        permissions: str) -> Response:
    """Set the permissions of a basic group for an object."""
    if (isinstance(object_id, int) and isinstance(group_id, int) and
            isinstance(permissions, str)):
        return putData(
            "objects/{}/permissions/groups/{}".format(object_id, group_id),
            permissions
        )
    else:
        raise TypeError()


def getAllProjectGroupsPermissions(object_id: int) -> Dict:
    """Get a mapping of project group IDs to their permissions."""
    if isinstance(object_id, int):
        return getData("objects/{}/permissions/projects".format(object_id))
    else:
        raise TypeError()


def getProjectGroupPermissions(object_id: int, project_id: int) -> str:
    """Get the permissions of a project group for an object."""
    if isinstance(object_id, int) and isinstance(project_id, int):
        return getData(
            "objects/{}/permissions/projects/{}" % (object_id, project_id)
        )
    else:
        raise TypeError()


def setProjectGroupPermissions(object_id: int, project_id: int,
                               permissions: str) -> Response:
    """Set the permissions of a project group for an object."""
    if (isinstance(object_id, int) and isinstance(project_id, int) and
            isinstance(permissions, str)):
        return putData(
            "objects/{}/permissions/projects/{}".format(object_id, project_id),
            permissions
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


def uploadFile(object_id: int, path: str) -> Response:
    """Create a new file with local storage for a specific object (object_id).

    Args:
        object_id (int): ID of the object
        path (str): Path of the file to be uploaded.
    """
    if isinstance(object_id, int) and isinstance(path, str):
        with open(path, "rb") as f:
            r = uploadFileRaw(object_id, os.path.basename(path), f)
        return r
    else:
        raise TypeError()


def uploadFileRaw(object_id: int, name: str, file_obj: BinaryIO) -> Response:
    """Create a new file with local storage for a specific object (object_id).

    Args:
        object_id (int): ID of the object
        name (str): Name that the file will have online.
        file_obj (BinaryIO): A binary stream that can be read to be uploaded.
    """
    if (isinstance(object_id, int) and isinstance(name, str) and
            isinstance(file_obj, IOBase)):
        base64encoded = base64.b64encode(file_obj.read())
        return postData("objects/{}/files/".format(object_id),
                        {"storage": "local", "original_file_name": name,
                         "base64_content": base64encoded.decode()})
    else:
        raise TypeError()


def postLink(object_id: int, url: str) -> Response:
    """Create a new file with url storage for a specific object (object_id)."""
    if isinstance(object_id, int) and isinstance(url, str):
        return postData("objects/{}/files/".format(object_id),
                        {"storage": "url", "url": url})
    else:
        raise TypeError()


"""Comments"""


def getCommentList(object_id: int) -> List:
    """Get a list of all comments for a specific object (object_id)."""
    if isinstance(object_id, int):
        return getData("objects/{}/comments".format(object_id))
    else:
        raise TypeError()


def getComment(object_id: int, comment_id: int) -> Dict:
    """Get specific comment (comment_id) for a specific object (object_id)."""
    if isinstance(object_id, int) and isinstance(comment_id, int):
        return getData("objects/{}/comments/{}".format(object_id, comment_id))
    else:
        raise TypeError()


def postComment(object_id: int, comment: str) -> Response:
    """Create a new comment for a specific object (object_id)."""
    if isinstance(object_id, int) and isinstance(comment, str):
        return postData("objects/{}/comments/".format(object_id),
                        {"content": comment})
    else:
        raise TypeError()
