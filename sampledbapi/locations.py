from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get"]


def getList() -> List:
    """Get a list of all locations.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#locations>`_
    """
    return getData("locations")


def get(location_id: int) -> Dict:
    """Get the specific location (location_id).

    Args:
        location_id (int): ID of the location to be retrieved.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#locations>`_
    """
    if isinstance(location_id, int):
        return getData("locations/{}".format(location_id))
    else:
        raise TypeError()
