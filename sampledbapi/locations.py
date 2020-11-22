from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList() -> List:
    """Get a list of all locations."""
    return getData("locations")


def get(location_id: int) -> Dict:
    """Get the specific location (location_id)."""
    if isinstance(location_id, int):
        return getData("locations/{}".format(location_id))
    else:
        raise TypeError()
