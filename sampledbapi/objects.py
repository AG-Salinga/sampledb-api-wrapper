from __future__ import annotations

import base64
import os
from datetime import datetime
from io import IOBase
from typing import BinaryIO, Dict, List

from requests import Response

from sampledbapi import SampleDBObject, getData, locations, postData, putData
from sampledbapi.users import User

__all__ = ["Object", "LocationOccurence", "Comment", "getList", "get",
           "create"]


class Object(SampleDBObject):

    object_id: int = None
    version_id: int = None
    action_id: int = None
    schema: dict = None
    data: dict = None

    def __repr__(self) -> str:
        return f"Object {self.object_id}"

    def getVersion(self, version_id: int) -> Object:
        """Get the specific version (version_id).

        Args:
            version_id (int): ID of the version to be retrieved.

        Returns:
            Object: Requested :class:`~sampledbapi.objects.Object`.
        """
        if isinstance(version_id, int):
            return Object(getData(
                f"objects/{self.object_id}/versions/{version_id}"
            ))
        else:
            raise TypeError()

    def update(self, data: dict) -> Response:
        """Create a new version.

        The data is a dictionary that has to be formatted according to the
        action's schema. Exemplary data:

        .. code-block::

            {"name": {
                "_type": "text",
                "text": "Example Object"
            }}

        """
        if isinstance(data, dict):
            return postData(f"objects/{self.object_id}/versions/",
                            {"data": data})
        else:
            raise TypeError()

    def getPublic(self) -> bool:
        """Get whether or not the object is public.

        Returns:
            bool: Whether the object is public or not.
        """
        return getData(f"objects/{self.object_id}/permissions/public")

    def setPublic(self, public: bool) -> Response:
        """Set whether or not the object is public.

        Args:
            public (bool): Whether the object is public or not.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(public, bool):
            return putData(f"objects/{self.object_id}/permissions/public",
                           public)
        else:
            raise TypeError()

    def getAllUsersPermissions(self) -> Dict:
        """Get a mapping of user IDs to their permissions.

        Returns:
            Dict: Mapping of user IDs to permissions.
        """
        return getData(f"objects/{self.object_id}/permissions/users")

    def getUserPermissions(self, user_id: int) -> str:
        """Get the permissions of a user.

        Args:
            user_id (int): ID of the user.

        Returns:
            str: Permissions of user for the object.
        """
        if isinstance(user_id, int):
            return getData(
                f"objects/{self.object_id}/permissions/users/{user_id}"
            )
        else:
            raise TypeError()

    def setUserPermissions(self, user_id: int, permissions: str) -> Response:
        """Set the permissions of a user.

        Args:
            user_id (int): ID of the user.
            permissions (str): Permissions of user for the object.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(user_id, int) and isinstance(permissions, str):
            return putData(
                f"objects/{self.object_id}/permissions/users/{user_id}",
                permissions
            )
        else:
            raise TypeError()

    def getAllGroupsPermissions(self) -> Dict:
        """Get a mapping of basic group IDs to their permissions.

        Returns:
            Dict: Mapping of group IDs to permissions.
        """
        return getData(f"objects/{self.object_id}/permissions/groups")

    def getGroupPermissions(self, group_id: int) -> str:
        """Get the permissions of a basic group.

        Args:
            group_id (int): ID of the group.

        Returns:
            str: Permissions of group for the object.
        """
        if isinstance(group_id, int):
            return getData(
                f"objects/{self.object_id}/permissions/groups/{group_id}"
            )
        else:
            raise TypeError()

    def setGroupPermissions(self, group_id: int, permissions: str) -> Response:
        """Set the permissions of a basic group.

        Args:
            group_id (int): ID of the group.
            permissions (str): Permissions of group for the object.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(group_id, int) and isinstance(permissions, str):
            return putData(
                f"objects/{self.object_id}/permissions/groups/{group_id}",
                permissions
            )
        else:
            raise TypeError()

    def getAllProjectGroupsPermissions(self) -> Dict:
        """Get a mapping of project group IDs to their permissions.

        Returns:
            Dict: Mapping of project group IDs to permissions.
        """
        return getData(f"objects/{self.object_id}/permissions/projects")

    def getProjectGroupPermissions(self, project_id: int) -> str:
        """Get the permissions of a project group.

        Args:
            project_id (int): ID of the project group.

        Returns:
            str: Permissions of project group for the object.
        """
        if isinstance(project_id, int):
            return getData(
                f"objects/{self.object_id}/permissions/projects/{project_id}"
            )
        else:
            raise TypeError()

    def setProjectGroupPermissions(self, project_id: int,
                                   permissions: str) -> Response:
        """Set the permissions of a project group.

        Args:
            project_id (int): ID of the project group.
            permissions (str): Permissions of project group for the object.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(project_id, int) and isinstance(permissions, str):
            return putData(
                f"objects/{self.object_id}/permissions/projects/{project_id}",
                permissions
            )
        else:
            raise TypeError()

    def getLocationList(self) -> List[locations.Location]:
        """Get a list of all object locations assignments.

        Returns:
            List: List of :class:`~sampledbapi.locations.Location`.
        """
        return [locations.Location(loc)
                for loc in getData(f"objects/{self.object_id}/locations")]

    def getLocation(self, location_id: int) -> locations.Location:
        """Get a specific object location assignment (location_id).

        Args:
            location_id (int): ID of the location.

        Returns:
            Location: The requested :class:`~sampledbapi.locations.Location`.
        """
        if isinstance(location_id, int):
            return locations.Location(getData(
                f"objects/{self.object_id}/locations/{location_id}")
            )

    def getFileList(self) -> List:
        """Get a list of all files.

        Returns:
            List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        return getData(f"objects/{self.object_id}/files")

    def getFileInfo(self, file_id: int) -> Dict:
        """Get a specific file (file_id).

        Args:
            file_id (int): ID of the file.

        Returns:
            Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(file_id, int):
            return getData(
                f"objects/{self.object_id}/files/{file_id}"
            )
        else:
            raise TypeError()

    def uploadFile(self, path: str) -> Response:
        """Create a new file with local storage.

        Args:
            path (str): Path of the file to be uploaded.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(path, str):
            with open(path, "rb") as f:
                r = self.uploadFileRaw(
                    self.object_id, os.path.basename(path), f)
            return r
        else:
            raise TypeError()

    def uploadFileRaw(self, name: str, file_obj: BinaryIO) -> Response:
        """Create a new file with local storage.

        Args:
            name (str): Name that the file will have online.
            file_obj (BinaryIO): A binary stream that can be read to be uploaded.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(name, str) and isinstance(file_obj, IOBase):
            base64encoded = base64.b64encode(file_obj.read())
            return postData(f"objects/{self.object_id}/files/",
                            {"storage": "local", "original_file_name": name,
                             "base64_content": base64encoded.decode()})
        else:
            raise TypeError()

    def postLink(self, url: str) -> Response:
        """Create a new file with url storage.

        Args:
            url (str): URL to be stored.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(url, str):
            return postData(f"objects/{self.object_id}/files/",
                            {"storage": "url", "url": url})
        else:
            raise TypeError()

    def getCommentList(self) -> List[Comment]:
        """Get a list of all comments.

        Returns:
            List: List of :class:`~sampledbapi.objects.Comment`.
        """
        return [Comment(c)
                for c in getData(f"objects/{self.object_id}/comments")]

    def getComment(self, comment_id: int) -> Comment:
        """Get specific comment (comment_id).

        Args:
            comment_id (int): ID of the comment.

        Returns:
            Object: Requested :class:`~sampledbapi.objects.Comment`.
        """
        if isinstance(comment_id, int):
            return Comment(
                Comment(getData(
                    f"objects/{self.object_id}/comments/{comment_id}"))
            )
        else:
            raise TypeError()

    def postComment(self, comment: str) -> Response:
        """Create a new comment.

        Args:
            comment (str): Comment to be posted.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#comments>`__
        """
        if isinstance(comment, str):
            return postData(f"objects/{self.object_id}/comments/",
                            {"content": comment})
        else:
            raise TypeError()


class LocationOccurence(SampleDBObject):

    object_id: int = None
    location: locations.Location = None
    responsible_user: User = None
    user: User = None
    description: str = None
    datetime: datetime = None

    def __repr__(self) -> str:
        return f"LocationOccurence of object {self.object_id} " \
            + "(at {self.location.name})"


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
        q (str): Search string for advanced search, `see here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/user_guide/objects.html#advanced-search>`__
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
            s += f"{p}={pars[p]}"
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
        return Object(getData(f"objects/{object_id}"))
    else:
        raise TypeError()


def create(action_id: int, data: dict) -> Response:
    """Create a new object.

    The data is a dictionary that has to be formatted according to the action's
    schema. Exemplary data:

    .. code-block::

        {"name": {
            "_type": "text",
            "text": "Example Object"
        }}

    """
    if isinstance(action_id, int) and isinstance(data, dict):
        return postData("objects/", {"action_id": action_id, "data": data})
    else:
        raise TypeError()


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

    def __str__(self) -> str:
        return f"Comment on object {self.object_id}, " \
            + f"posted {self.utc_datetime}"
