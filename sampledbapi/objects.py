from typing import Dict, List

from sampledbapi import getData

def getList() -> List:
    """Get a list of all objects visible to the current user.

    The list only contains the current version of each object. By passing the parameter q to the query,
    the Advanced Search can be used. By passing the parameters action_id or action_type objects can be
    filtered by the action they were created with or by their type (e.g. sample or measurement)."""

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
