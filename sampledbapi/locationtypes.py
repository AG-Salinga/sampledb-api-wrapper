from typing import List, Optional

from sampledbapi import SampleDBObject, get_data

__all__ = ["LocationType", "get_list", "get"]


class LocationType(SampleDBObject):

    location_type_id: Optional[int] = None
    name: Optional[str] = None

    def __repr__(self) -> str:
        return f"LocationType {self.location_type_id} ({self.name})"


def get_list() -> List[LocationType]:
    """Get a list of all location types.

    Returns:
        List: List of :class:`~sampledbapi.locationtypes.LocationType` objects.
    """
    return [LocationType(loct) for loct in get_data("location_types")]


def get(location_type_id: int) -> LocationType:
    """Get the specific location type (location_type_id).

    Args:
        location_type_id (int): ID of the location to be retrieved.

    Returns:
        Location: The requested :class:`~sampledbapi.locationtypes.LocationType`.
    """
    if isinstance(location_type_id, int):
        return LocationType(get_data(f"location_types/{location_type_id}"))
    else:
        raise TypeError()
