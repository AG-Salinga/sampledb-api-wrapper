from typing import List

from sampledbapi import SampleDBObject, getData

__all__ = ["Location", "getList", "get"]


class Location(SampleDBObject):

    location_id: int = None
    name: str = None
    description: str = None
    parent_location_id: int = None


def getList() -> List[Location]:
    """Get a list of all locations.

    Returns:
        List: List of :class:`~sampledbapi.locations.Location` objects.
    """
    return [Location(loc) for loc in getData("locations")]


def get(location_id: int) -> Location:
    """Get the specific location (location_id).

    Args:
        location_id (int): ID of the location to be retrieved.

    Returns:
        Location: The requested :class:`~sampledbapi.locations.Location`.
    """
    if isinstance(location_id, int):
        return Location(getData("locations/{}".format(location_id)))
    else:
        raise TypeError()
