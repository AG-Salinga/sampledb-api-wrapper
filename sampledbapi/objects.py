from __future__ import annotations

import base64
from datetime import datetime
from io import IOBase
from typing import BinaryIO, Dict, List, Optional, Any

from requests import Response

from sampledbapi import SampleDBObject, get_data, locations, users, post_data, put_data
from sampledbapi.users import User

__all__ = ["Object", "File", "Comment", "get_list", "get", "create"]


class Object(SampleDBObject):

    object_id: Optional[int] = None
    version_id: Optional[int] = None
    action_id: Optional[int] = None
    schema: Optional[dict] = None
    data: Optional[dict] = None

    def __repr__(self) -> str:
        return f"Object {self.object_id}"

    def get_version(self, version_id: int) -> Object:
        """Get the specific version (version_id).

        Args:
            version_id (int): ID of the version to be retrieved.

        Returns:
            Object: Requested :class:`~sampledbapi.objects.Object`.
        """
        if isinstance(version_id, int):
            return Object(get_data(
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
            return post_data(f"objects/{self.object_id}/versions/",
                             {"data": data})
        else:
            raise TypeError()

    def get_public(self) -> bool:
        """Get whether or not the object is public.

        Returns:
            bool: Whether the object is public or not.
        """
        return get_data(f"objects/{self.object_id}/permissions/public")

    def set_public(self, public: bool) -> Response:
        """Set whether or not the object is public.

        Args:
            public (bool): Whether the object is public or not.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(public, bool):
            return put_data(f"objects/{self.object_id}/permissions/public",
                            public)
        else:
            raise TypeError()

    def get_all_user_permissions(self) -> Dict:
        """Get a mapping of user IDs to their permissions.

        Returns:
            Dict: Mapping of user IDs to permissions.
        """
        return get_data(f"objects/{self.object_id}/permissions/users")

    def get_user_permissions(self, user_id: int) -> str:
        """Get the permissions of a user.

        Args:
            user_id (int): ID of the user.

        Returns:
            str: Permissions of user for the object.
        """
        if isinstance(user_id, int):
            return get_data(
                f"objects/{self.object_id}/permissions/users/{user_id}"
            )
        else:
            raise TypeError()

    def set_user_permissions(self, user_id: int, permissions: str) -> Response:
        """Set the permissions of a user.

        Args:
            user_id (int): ID of the user.
            permissions (str): Permissions of user for the object.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(user_id, int) and isinstance(permissions, str):
            return put_data(
                f"objects/{self.object_id}/permissions/users/{user_id}",
                permissions
            )
        else:
            raise TypeError()

    def get_all_group_permissions(self) -> Dict:
        """Get a mapping of basic group IDs to their permissions.

        Returns:
            Dict: Mapping of group IDs to permissions.
        """
        return get_data(f"objects/{self.object_id}/permissions/groups")

    def get_group_permissions(self, group_id: int) -> str:
        """Get the permissions of a basic group.

        Args:
            group_id (int): ID of the group.

        Returns:
            str: Permissions of group for the object.
        """
        if isinstance(group_id, int):
            return get_data(
                f"objects/{self.object_id}/permissions/groups/{group_id}"
            )
        else:
            raise TypeError()

    def set_group_permissions(self, group_id: int, permissions: str) -> Response:
        """Set the permissions of a basic group.

        Args:
            group_id (int): ID of the group.
            permissions (str): Permissions of group for the object.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(group_id, int) and isinstance(permissions, str):
            return put_data(
                f"objects/{self.object_id}/permissions/groups/{group_id}",
                permissions
            )
        else:
            raise TypeError()

    def get_all_project_group_permissions(self) -> Dict:
        """Get a mapping of project group IDs to their permissions.

        Returns:
            Dict: Mapping of project group IDs to permissions.
        """
        return get_data(f"objects/{self.object_id}/permissions/projects")

    def get_project_group_permissions(self, project_id: int) -> str:
        """Get the permissions of a project group.

        Args:
            project_id (int): ID of the project group.

        Returns:
            str: Permissions of project group for the object.
        """
        if isinstance(project_id, int):
            return get_data(
                f"objects/{self.object_id}/permissions/projects/{project_id}"
            )
        else:
            raise TypeError()

    def set_project_group_permissions(self, project_id: int,
                                      permissions: str) -> Response:
        """Set the permissions of a project group.

        Args:
            project_id (int): ID of the project group.
            permissions (str): Permissions of project group for the object.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#object-permissions>`__
        """
        if isinstance(project_id, int) and isinstance(permissions, str):
            return put_data(
                f"objects/{self.object_id}/permissions/projects/{project_id}",
                permissions
            )
        else:
            raise TypeError()

    def get_location_occurences(self) -> List[LocationOccurence]:
        """
        Get a list of all object locations assignments for a specific object.

        Args:

        Returns:
            List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#reading-a-list-of-an-object-s-locations>`__

        """
        return [LocationOccurence(i) for i in get_data(f"objects/{self.object_id}/locations")]

    def get_location_occurence(self, location_id: int) -> LocationOccurence:
        """
        Get a specific object location assignment (index) for a specific object.

        Args:
            location_id (int) : ID of the location

        Returns:
            LocationOccurence: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#reading-an-object-s-location>`__


        """
        if isinstance(location_id, int):
            return LocationOccurence(get_data(
                f"objects/{self.object_id}/locations/{location_id}"
            ))
        else:
            raise TypeError()

    def get_file_list(self) -> List:
        """Get a list of all files.

        Returns:
            List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        return [File(i) for i in get_data(f"objects/{self.object_id}/files")]

    def get_file(self, file_id: int) -> File:
        """Get a specific file (file_id).

        Args:
            file_id (int): ID of the file.

        Returns:
            Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(file_id, int):
            return File(get_data(
                f"objects/{self.object_id}/files/{file_id}"
            ))
        else:
            raise TypeError()

    def upload_file(self, path: str, name: Optional[str] = None) -> Response:
        """Create a new file with local storage.

        Args:
            path (str): Path of the file to be uploaded.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(path, str):
            with open(path, "rb") as f:
                f.name
                r = self.upload_file_raw(f.name if name is None else name, f)
            return r
        else:
            raise TypeError()

    def upload_file_raw(self, name: str, file_obj: BinaryIO) -> Response:
        """Create a new file with local storage.

        Args:
            name (str): Name that the file will have online.
            file_obj (BinaryIO): A binary stream that can be read to be uploaded.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(name, str) and isinstance(file_obj, IOBase):
            base64encoded = base64.b64encode(file_obj.read())
            return post_data(f"objects/{self.object_id}/files/",
                             {"storage": "local", "original_file_name": name,
                              "base64_content": base64encoded.decode()})
        else:
            raise TypeError()

    def post_link(self, url: str) -> Response:
        """Create a new file with url storage.

        Args:
            url (str): URL to be stored.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#files>`__
        """
        if isinstance(url, str):
            return post_data(f"objects/{self.object_id}/files/",
                             {"storage": "url", "url": url})
        else:
            raise TypeError()

    def get_comment_list(self) -> List[Comment]:
        """Get a list of all comments.

        Returns:
            List: List of :class:`~sampledbapi.objects.Comment`.
        """
        return [Comment(c)
                for c in get_data(f"objects/{self.object_id}/comments")]

    def get_comment(self, comment_id: int) -> Comment:
        """Get specific comment (comment_id).

        Args:
            comment_id (int): ID of the comment.

        Returns:
            Object: Requested :class:`~sampledbapi.objects.Comment`.
        """
        if isinstance(comment_id, int):
            return Comment(get_data(
                f"objects/{self.object_id}/comments/{comment_id}"))
        else:
            raise TypeError()

    def post_comment(self, comment: str) -> Response:
        """Create a new comment.

        Args:
            comment (str): Comment to be posted.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#comments>`__
        """
        if isinstance(comment, str):
            return post_data(f"objects/{self.object_id}/comments/",
                             {"content": comment})
        else:
            raise TypeError()


def get_list(q: str = "", action_id: int = -1, action_type: str = "",
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
        pars: Dict[str, Any] = {}
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

        return [Object(o) for o in get_data(s)]
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
        return Object(get_data(f"objects/{object_id}"))
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
        return post_data("objects/", {"action_id": action_id, "data": data})
    else:
        raise TypeError()


class File(SampleDBObject):

    object_id: Optional[int] = None
    file_id: Optional[int] = None
    storage: Optional[str] = None
    original_file_name: Optional[str] = None
    base64_content: Optional[str] = None

    def __repr__(self) -> str:
        return f"File {self.file_id}, " \
            + f"Name {self.original_file_name}"


class LocationOccurence(SampleDBObject):

    object_id: Optional[int] = None
    location: Optional[locations.Location] = None
    responsible_user: Optional[User] = None
    user: Optional[User] = None
    description: Optional[str] = None
    utc_datetime: Optional[datetime] = None

    def __init__(self, d: Dict):
        """Initialize a new instrument from dictionary."""
        super().__init__(d)
        if "location" in d:
            self.location = locations.get(d["location"])
        if "responsible_user" in d:
            self.responsible_user = users.get(d["responsible_user"])
        if "user" in d:
            self.user = users.get(d["user"])
        if "utc_datetime" in d:
            self.utc_datetime = datetime.strptime(
                d["utc_datetime"], '%Y-%m-%dT%H:%M:%S.%f')

    def __repr__(self) -> str:
        return f"LocationOccurence of object {self.object_id} " \
            + "(at {self.location.name})"


class Comment(SampleDBObject):

    object_id: Optional[int] = None
    user_id: Optional[int] = None
    comment_id: Optional[int] = None
    content: Optional[str] = None
    utc_datetime: Optional[datetime] = None

    def __init__(self, d: Dict):
        """Initialize a new comment from dictionary."""
        super().__init__(d)
        if "utc_datetime" in d:
            self.utc_datetime = datetime.strptime(
                d["utc_datetime"], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self) -> str:
        return f"Comment on object {self.object_id}, " \
            + f"posted {self.utc_datetime}"
