from typing import List, Optional

from sampledbapi import SampleDBObject, get_data

__all__ = ["Location", "get_list", "get"]


class Location(SampleDBObject):

    location_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    parent_location_id: Optional[int] = None
    type_id: Optional[int] = None
    is_hidden: Optional[bool] = None

    def __repr__(self) -> str:
        return f"Location {self.location_id} ({self.name})"


def get_list() -> List[Location]:
    """Get a list of all locations.

    Returns:
        List: List of :class:`~sampledbapi.locations.Location` objects.
    """
    return [Location(loc) for loc in get_data("locations")]


def get(location_id: int) -> Location:
    """Get the specific location (location_id).

    Args:
        location_id (int): ID of the location to be retrieved.

    Returns:
        Location: The requested :class:`~sampledbapi.locations.Location`.
    """
    if isinstance(location_id, int):
        return Location(get_data(f"locations/{location_id}"))
    else:
        raise TypeError()
