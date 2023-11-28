import typing
from datetime import datetime

from .comm import get_data, SampleDBObject

__all__ = ["ObjectLogEntry", "get_object_log_entries"]


class ObjectLogEntry(SampleDBObject):

    log_entry_id: typing.Optional[int] = None
    type: typing.Optional[str] = None
    object_id: typing.Optional[int] = None
    user_id: typing.Optional[int] = None
    data: typing.Optional[typing.Dict[str, typing.Any]] = None
    utc_datetime: typing.Optional[datetime] = None

    def __repr__(self) -> str:
        return f"ObjectLogEntry {self.log_entry_id}"


def get_object_log_entries(after_id: typing.Optional[int] = None) -> typing.List[ObjectLogEntry]:
    """Query the contents of this object's object log.

    Args:
        after_id (int): only log entries created after the entry with the id after_id are returned

    Returns:
        List: List of :class:`~sampledbapi.object_log.ObjectLogEntry`.
    """
    if after_id is None:
        return [ObjectLogEntry(entry) for entry in get_data('object_log_entries/')]
    if isinstance(after_id, int):
        return [ObjectLogEntry(entry) for entry in get_data('object_log_entries/', params={'after_id': after_id})]
    else:
        raise TypeError()
