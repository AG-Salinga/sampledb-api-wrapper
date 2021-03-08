import base64
import os
from datetime import datetime
from io import IOBase
from sampledbapi.users import User
from typing import BinaryIO, Dict, List

from requests import Response

from sampledbapi import SampleDBObject, getData, locations, postData, putData

__all__ = ["Object", "getList", "get", "getVersion", "create", "update",
           "getPublic", "setPublic", "getAllUsersPermissions",
           "getUserPermissions", "setUserPermissions",
           "getAllGroupsPermissions", "getGroupPermissions",
           "setGroupPermissions", "getAllProjectGroupsPermissions",
           "getProjectGroupPermissions", "setProjectGroupPermissions",
           "getLocationList", "getLocation", "getFileList", "getFileInfo",
           "uploadFile", "uploadFileRaw", "postLink", "getCommentList",
           "getComment", "postComment"]


class Object(SampleDBObject):

    object_id: int = None
    version_id: int = None
    action_id: int = None
    schema: dict = None
    data: dict = None


class LocationOccurence(SampleDBObject):

    object_id: int = None
    location: locations.Location = None
    responsible_user: User = None
    user: User = None
    description: str = None
    datetime: datetime = None


def getList(q: str = "", action_id: int = -1, action_type: str = "",
            limit: int = -1, offset: int = -1,
            name_only: bool = False) -> List[Object]:
    """Get a list of all objects visible to the current user.

    The list only contains the current version of each object. By passing the
    parameter q to the query, the Advanced Search can be used. By passing the
    parameters action_id or action_type objects can be filtered by the action
    they were created with or by their type (e.g. sample or measurement).

    Instead of returning all objects, the parameters limit and offset can be
    used to reduce to maximum number of objects returned and to provide an
    offset in the returned set, so allow simple pagination.

    If the parameter name_only is provided, the object data and schema will be
    reduced to the name property, omitting all other properties and schema
    information.

    Args:
        q (str): Search string for advanced search, `see here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/user_guide/objects.html#advanced-search>`_
        action_id (int): Filter by action ID.
        action_type (str): Filter by action type.
        limit (int): Limit number of results (helpful for pagination).
        offset (int): Offset for limited retrieval of results (pagination).
        name_only (bool): Only names will be returned, no other information.

    Returns:
        List: List of :class:`~sampledbapi.objects.Object`.
    """
    if (isinstance(q, str) and isinstance(action_id, int) and
            isinstance(action_type, str) and isinstance(limit, int) and
            isinstance(offset, int) and isinstance(name_only, bool)):
        s = "objects"
        pars = {}
        if q != "":
            pars["q"] = q
        if action_id > 0:
            pars["action_id"] = action_id
        if action_type != "":
            pars["action_type"] = action_type
        if limit > 0:
            pars["limit"] = limit
        if offset > 0:
            pars["offset"] = offset
        if name_only:
            pars["name_only"] = "true"

        if len(pars) > 0:
            s += "?"
        for i, p in enumerate(pars):
            s += "{}={}".format(p, pars[p])
            if i < len(pars) - 1:
                s += "&"

        return [Object(o) for o in getData(s)]
    else:
        raise TypeError()


def get(object_id: int) -> Object:
    """Get the current version of an object (object_id).

    Args:
        object_id (int): ID of the object.

    Returns:
        Object: Requested :class:`~sampledbapi.objects.Object`.
    """
    if isinstance(object_id, int):
        return Object(getData("objects/{}".format(object_id)))
    else:
        raise TypeError()


def getVersion(object_id: int, version_id: int) -> Object:
    """Get the specific version (version_id) of an object (object_id).

    Args:
        object_id (int): ID of the object.
        version_id (int): ID of the version to be retrieved.

    Returns:
        Object: Requested :class:`~sampledbapi.objects.Object`.
    """
    if isinstance(object_id, int) and isinstance(version_id, int):
        return Object(getData(
            "objects/{}/versions/{}".format(object_id, version_id)
        ))
    else:
        raise TypeError()


def create(action_id: int, data: dict) -> Response:
    """Create a new object.

    The data is a dictionary that has to be formatted according to the action's
    schema. Exemplary data:
    ```
    {"name": {
        "_type": "text",
        "text": "Example Object"
    }}
    ```
    """
    if isinstance(action_id, int) and isinstance(data, dict):
        return postData("objects/", {"action_id": action_id, "data": data})
    else:
        raise TypeError()


def update(object_id: int, data: dict) -> Response:
    """Create a new version of an object (object_id).

    The data is a dictionary that has to be formatted according to the action's
    schema. Exemplary data:
    ```
    {"name": {
        "_type": "text",
        "text": "Example Object"
    }}
    """
    if isinstance(object_id, int) and isinstance(data, dict):
        return postData("objects/{}/versions/".format(object_id),
                        {"data": data})
    else:
        raise TypeError()


"""Permissions"""


def getPublic(object_id: int) -> bool:
    """Get whether or not an object is public.

    Args:
        object_id (int): ID of the object.

    Returns:
        bool: Whether the object is public or not.
    """
    if isinstance(object_id, int):
        return getData("objects/{}/permissions/public".format(object_id))
    else:
        raise TypeError()


def setPublic(object_id: int, public: bool) -> Response:
    """Set whether or not an object is public.

    Args:
        object_id (int): ID of the object.
        public (bool): Whether the object is public or not.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`_
    """
    if isinstance(object_id, int) and isinstance(public, bool):
        return putData("objects/{}/permissions/public".format(object_id),
                       public)
    else:
        raise TypeError()


def getAllUsersPermissions(object_id: int) -> Dict:
    """Get a mapping of user IDs to their permissions.

    Args:
        object_id (int): ID of the object.

    Returns:
        Dict: Mapping of user IDs to permissions.
    """
    if isinstance(object_id, int):
        return getData("objects/{}/permissions/users".format(object_id))
    else:
        raise TypeError()


def getUserPermissions(object_id: int, user_id: int) -> str:
    """Get the permissions of a user for an object.

    Args:
        object_id (int): ID of the object.
        user_id (int): ID of the user.

    Returns:
        str: Permissions of user for the object.
    """
    if isinstance(object_id, int) and isinstance(user_id, int):
        return getData(
            "objects/{}/permissions/users/{}".format(object_id, user_id)
        )
    else:
        raise TypeError()


def setUserPermissions(object_id: int, user_id: int,
                       permissions: str) -> Response:
    """Set the permissions of a user for an object.

    Args:
        object_id (int): ID of the object.
        user_id (int): ID of the user.
        permissions (str): Permissions of user for the object.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`_
    """
    if (isinstance(object_id, int) and isinstance(user_id, int) and
            isinstance(permissions, str)):
        return putData(
            "objects/{}/permissions/users/{}".format(object_id, user_id),
            permissions
        )
    else:
        raise TypeError()


def getAllGroupsPermissions(object_id: int) -> Dict:
    """Get a mapping of basic group IDs to their permissions.

    Args:
        object_id (int): ID of the object.

    Returns:
        Dict: Mapping of group IDs to permissions.
    """
    if isinstance(object_id, int):
        return getData("objects/{}/permissions/groups".format(object_id))
    else:
        raise TypeError()


def getGroupPermissions(object_id: int, group_id: int) -> str:
    """Get the permissions of a basic group for an object.

    Args:
        object_id (int): ID of the object.
        group_id (int): ID of the group.

    Returns:
        str: Permissions of group for the object.
    """
    if isinstance(object_id, int) and isinstance(group_id, int):
        return getData(
            "objects/{}/permissions/groups/{}".format(object_id, group_id)
        )
    else:
        raise TypeError()


def setGroupPermissions(object_id: int, group_id: int,
                        permissions: str) -> Response:
    """Set the permissions of a basic group for an object.

    Args:
        object_id (int): ID of the object.
        group_id (int): ID of the group.
        permissions (str): Permissions of group for the object.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`_
    """
    if (isinstance(object_id, int) and isinstance(group_id, int) and
            isinstance(permissions, str)):
        return putData(
            "objects/{}/permissions/groups/{}".format(object_id, group_id),
            permissions
        )
    else:
        raise TypeError()


def getAllProjectGroupsPermissions(object_id: int) -> Dict:
    """Get a mapping of project group IDs to their permissions.

    Args:
        object_id (int): ID of the object.

    Returns:
        Dict: Mapping of project group IDs to permissions.
    """
    if isinstance(object_id, int):
        return getData("objects/{}/permissions/projects".format(object_id))
    else:
        raise TypeError()


def getProjectGroupPermissions(object_id: int, project_id: int) -> str:
    """Get the permissions of a project group for an object.

    Args:
        object_id (int): ID of the object.
        project_id (int): ID of the project group.

    Returns:
        str: Permissions of project group for the object.
    """
    if isinstance(object_id, int) and isinstance(project_id, int):
        return getData(
            "objects/{}/permissions/projects/{}".format(object_id, project_id)
        )
    else:
        raise TypeError()


def setProjectGroupPermissions(object_id: int, project_id: int,
                               permissions: str) -> Response:
    """Set the permissions of a project group for an object.

    Args:
        object_id (int): ID of the object.
        project_id (int): ID of the project group.
        permissions (str): Permissions of project group for the object.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`_
    """
    if (isinstance(object_id, int) and isinstance(project_id, int) and
            isinstance(permissions, str)):
        return putData(
            "objects/{}/permissions/projects/{}".format(object_id, project_id),
            permissions
        )
    else:
        raise TypeError()


"""Locations"""


def getLocationList(object_id: int) -> List[locations.Location]:
    """Get a list of all object locations assignments for a specific object (object_id).

    Args:
        object_id (int): ID of the object.

    Returns:
        List: List of :class:`~sampledbapi.locations.Location`.
    """
    if isinstance(object_id, int):
        return [locations.Location(loc)
                for loc in getData("objects/{}/locations".format(object_id))]
    else:
        raise TypeError()


def getLocation(object_id: int, location_id: int) -> locations.Location:
    """Get a specific object location assignment (location_id) for a specific object (object_id).

    Args:
        object_id (int): ID of the object.
        location_id (int): ID of the location.

    Returns:
        Location: The requested :class:`~sampledbapi.locations.Location`.
    """
    if isinstance(object_id, int) and isinstance(location_id, int):
        return locations.Location(getData(
            "objects/{}/locations/{}".format(object_id, location_id)
        ))
    else:
        raise TypeError()


"""Files"""


def getFileList(object_id: int) -> List:
    """Get a list of all files for a specific object (object_id).

    Args:
        object_id (int): ID of the object.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`_
    """
    if isinstance(object_id, int):
        return getData("objects/{}/files".format(object_id))
    else:
        raise TypeError()


def getFileInfo(object_id: int, file_id: int) -> Dict:
    """Get a specific file (file_id) for a specific object (object_id).

    Args:
        object_id (int): ID of the object.
        file_id (int): ID of the file.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`_
    """
    if isinstance(object_id, int) and isinstance(file_id, int):
        return getData(
            "objects/{}/files/{}".format(object_id, file_id)
        )
    else:
        raise TypeError()


def uploadFile(object_id: int, path: str) -> Response:
    """Create a new file with local storage for a specific object (object_id).

    Args:
        object_id (int): ID of the object.
        path (str): Path of the file to be uploaded.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`_
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
        object_id (int): ID of the object.
        name (str): Name that the file will have online.
        file_obj (BinaryIO): A binary stream that can be read to be uploaded.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`_
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
    """Create a new file with url storage for a specific object (object_id).

    Args:
        object_id (int): ID of the object.
        url (str): URL to be stored.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`_
    """
    if isinstance(object_id, int) and isinstance(url, str):
        return postData("objects/{}/files/".format(object_id),
                        {"storage": "url", "url": url})
    else:
        raise TypeError()


"""Comments"""


class Comment(SampleDBObject):

    object_id: int = None
    user_id: int = None
    comment_id: int = None
    content: str = None
    utc_datetime: datetime = None

    def __init__(self, d: Dict = None):
        """Initialize a new comment from dictionary."""
        super().__init__(d)
        if d is not None and "utc_datetime" in d:
            self.utc_datetime = datetime.strptime(d["utc_datetime"])


def getCommentList(object_id: int) -> List[Comment]:
    """Get a list of all comments for a specific object (object_id).

    Args:
        object_id (int): ID of the object.

    Returns:
        List: List of :class:`~sampledbapi.objects.Comment`.
    """
    if isinstance(object_id, int):
        return [Comment(c)
                for c in getData("objects/{}/comments".format(object_id))]
    else:
        raise TypeError()


def getComment(object_id: int, comment_id: int) -> Comment:
    """Get specific comment (comment_id) for a specific object (object_id).

    Args:
        object_id (int): ID of the object.
        comment_id (int): ID of the comment.

    Returns:
        Object: Requested :class:`~sampledbapi.objects.Comment`.
    """
    if isinstance(object_id, int) and isinstance(comment_id, int):
        return Comment(
            Comment(getData(
                "objects/{}/comments/{}".format(object_id, comment_id)))
        )
    else:
        raise TypeError()


def postComment(object_id: int, comment: str) -> Response:
    """Create a new comment for a specific object (object_id).

    Args:
        object_id (int): ID of the object.
        comment (str): Comment to be posted.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#comments>`_
    """
    if isinstance(object_id, int) and isinstance(comment, str):
        return postData("objects/{}/comments/".format(object_id),
                        {"content": comment})
    else:
        raise TypeError()
