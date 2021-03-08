import base64
import os
from datetime import datetime
from typing import Dict, List

from requests import Response

from sampledbapi import SampleDBObject, getData, postData, users

__all__ = ["Instrument", "getList", "get", "getLogEntryList", "getLogEntry",
           "getLogCategoryList", "getLogCategory",
           "getFileAttachmentList", "getFileAttachment",
           "getObjectAttachmentList", "getObjectAttachment", "createLogEntry"]


class Instrument(SampleDBObject):

    instrument_id: int = None
    name: str = None
    description: str = None
    is_hidden: bool = None
    instrument_scientists: List[users.User] = None

    def __init__(self, d: Dict = None):
        """Initialize a new instrument from dictionary."""
        super().__init__(d)
        if d is not None and "instrument_scientists" in d:
            self.instrument_scientists = [
                users.get(i) for i in d["instrument_scientists"]]


def getList() -> List[Instrument]:
    """Get a list of all instruments.

    Returns:
        List: List of :class:`~sampledbapi.instrument.Instrument` objects.
    """
    return [Instrument(i) for i in getData("instruments")]


def get(instrument_id: int) -> Dict:
    """Get the specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the specific instrument.

    Returns:
        Instrument: The requested :class:`~sampledbapi.instrument.Instrument`.
    """
    if isinstance(instrument_id, int):
        return Instrument(getData("instruments/{}".format(instrument_id)))
    else:
        raise TypeError()


"""Instrument log entries"""


class InstrumentLogCategory(SampleDBObject):

    category_id: int = None
    title: str = None


class InstrumentLogEntry(SampleDBObject):

    log_entry_id: int = None
    utc_datetime: datetime = None
    author: users.User = None
    content: str = None
    categories: List[InstrumentLogCategory] = None

    def __init__(self, d: Dict = None):
        """Initialize a new instrument from dictionary."""
        super().__init__(d)
        if d is not None:
            if "categories" in d:
                self.categories = [
                    InstrumentLogCategory(c) for c in d["categories"]]
            if "author" in d:
                self.author = users.get(d["author"])
            if "utc_datetime" in d:
                self.utc_datetime = datetime.strptime(d["utc_datetime"])


class InstrumentLogFileAttachment(SampleDBObject):

    file_attachment_id: int = None
    file_name: str = None
    content: str = None


class InstrumentLogObjectAttachment(SampleDBObject):

    object_attachment_id: int = None
    object_id: int = None


def getLogEntryList(instrument_id: int) -> List[InstrumentLogEntry]:
    """Get a list of all log entries for a specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the specific instrument.

    Returns:
        List: List of :class:`~sampledbapi.instrument.InstrumentLogEntry`.
    """
    if isinstance(instrument_id, int):
        return [InstrumentLogEntry(log) for log in getData(
            "instruments/{}/log_entries".format(instrument_id))]
    else:
        raise TypeError()


def getLogEntry(instrument_id: int, log_entry_id: int) -> InstrumentLogEntry:
    """Get the specific log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.

    Returns:
        InstrumentLogEntry: The requested
            :class:`~sampledbapi.instrument.InstrumentLogEntry`.
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return InstrumentLogEntry(getData(
            "instruments/{}/log_entries/{}".format(
                instrument_id, log_entry_id)))
    else:
        raise TypeError()


def getLogCategoryList(instrument_id: int) -> List[InstrumentLogCategory]:
    """Get a list of all log category for a specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.

    Returns:
        List: List of :class:`~sampledbapi.instrument.InstrumentLogCategory`.
    """
    if isinstance(instrument_id, int):
        return [InstrumentLogCategory(c) for c in getData(
            "instruments/{}/log_categories".format(instrument_id))]
    else:
        raise TypeError()


def getLogCategory(instrument_id: int,
                   log_category_id: int) -> InstrumentLogCategory:
    """Get the specific log category (log_category_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_category_id (int): ID of the specific log category.

    Returns:
        InstrumentLogCategory: The requested
            :class:`~sampledbapi.instrument.InstrumentLogCategory`.
    """
    if isinstance(instrument_id, int) and isinstance(log_category_id, int):
        return InstrumentLogCategory(getData(
            "instruments/{}/log_categories/{}".format(
                instrument_id, log_category_id)))
    else:
        raise TypeError()


def getFileAttachmentList(instrument_id: int, log_entry_id: int) -> List[
        InstrumentLogFileAttachment]:
    """Get a list of file attachments for a specific log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.

    Returns:
        List: List of
            :class:`~sampledbapi.instrument.InstrumentLogFileAttachment`.
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return [InstrumentLogFileAttachment(f) for f in getData(
            "instruments/{}/log_entries/{}/file_attachments".format(
                instrument_id, log_entry_id))]
    else:
        raise TypeError()


def getFileAttachment(instrument_id: int, log_entry_id: int,
                      file_attachment_id: int) -> InstrumentLogFileAttachment:
    """Get a specific file attachment (file_attachment_id) for a log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.
        file_attachment_id (int): ID of the file attachment.

    Returns:
        InstrumentLogFileAttachment: The requested
            :class:`~sampledbapi.instrument.InstrumentLogFileAttachment`.
    """
    if (isinstance(instrument_id, int) and isinstance(log_entry_id, int) and
            isinstance(file_attachment_id, int)):
        return InstrumentLogFileAttachment(getData(
            "instruments/{}/log_entries/{}/file_attachments/{}".format(
                instrument_id, log_entry_id, file_attachment_id)))
    else:
        raise TypeError()


def getObjectAttachmentList(instrument_id: int, log_entry_id: int) -> List[
        InstrumentLogObjectAttachment]:
    """Get a list of object attachments for a specific log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.

    Returns:
        List: List of
            :class:`~sampledbapi.instrument.InstrumentLogObjectAttachment`.
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return [InstrumentLogObjectAttachment(o) for o in getData(
            "instruments/{}/log_entries/{}/object_attachments".format(
                instrument_id, log_entry_id))]
    else:
        raise TypeError()


def getObjectAttachment(
        instrument_id: int, log_entry_id: int, object_attachment_id: int
) -> InstrumentLogObjectAttachment:
    """Get a specific object attachment (object_attachment_id) for a log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.
        object_attachment_id (int): ID of the object attachment.

    Returns:
        InstrumentLogObjectAttachment: The requested
            :class:`~sampledbapi.instrument.InstrumentLogObjectAttachment`.
    """
    if (isinstance(instrument_id, int) and isinstance(log_entry_id, int) and
            isinstance(object_attachment_id, int)):
        return InstrumentLogObjectAttachment(getData(
            "instruments/{}/log_entries/{}/object_attachments/{}".format(
                instrument_id, log_entry_id, object_attachment_id)))
    else:
        raise TypeError()


def createLogEntry(instrument_id: int, content: str, category_ids: List = [],
                   file_attachments: List = [],
                   object_attachments: List = []) -> Response:
    """Create a log entry for an instrument (instrument_id) and optionally attach files and objects to it.

    Args:
        instrument_id (int): Instrument ID for which the log entry is created.
        content (str): Log message.
        category_ids (list of ints): An optional list of category IDs for the log entry.
        file_attachments (list of strings): List of file paths to be read and attached to the log entry.
        object_attachments (list of integers): Object IDs to be attached to the log entry.

    Returns:
        HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if (isinstance(instrument_id, int) and isinstance(content, str) and
            isinstance(category_ids, list) and
            isinstance(file_attachments, list) and
            isinstance(object_attachments, list)):
        data = {"content": content}

        def conv_file(path: str):
            with open(path, "rb") as f:
                base64encoded = base64.b64encode(f.read())
            return {"file_name": os.path.basename(path),
                    "base64_content": base64encoded.decode()}

        if len(category_ids) > 0:
            data["category_ids"] = category_ids
        if len(file_attachments) > 0:
            data["file_attachments"] = [conv_file(f) for f in file_attachments]
        if len(object_attachments) > 0:
            data["object_attachments"] = [
                {"object_id": i} for i in object_attachments]

        return postData(
            "instruments/{}/log_entries/".format(instrument_id), data)
    else:
        raise TypeError()
