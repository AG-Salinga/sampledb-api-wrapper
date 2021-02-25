import base64
import os
from typing import Dict, List

from requests import Response

from sampledbapi import getData, postData

__all__ = ["getList", "get", "getLogEntryList", "getLogEntry",
           "getLogCategoryList", "getLogCategory",
           "getFileAttachmentList", "getFileAttachment",
           "getObjectAttachmentList", "getObjectAttachment", "createLogEntry"]


def getList() -> List:
    """Get a list of all instruments.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instruments>`_
    """
    return getData("instruments")


def get(instrument_id: int) -> Dict:
    """Get the specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the specific instrument.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int):
        return getData("instruments/{}".format(instrument_id))
    else:
        raise TypeError()


"""Instrument log entries"""


def getLogEntryList(instrument_id: int) -> List:
    """Get a list of all log entries for a specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the specific instrument.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int):
        return getData("instruments/{}/log_entries".format(instrument_id))
    else:
        raise TypeError()


def getLogEntry(instrument_id: int, log_entry_id: int) -> Dict:
    """Get the specific log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return getData("instruments/{}/log_entries/{}".format(
            instrument_id, log_entry_id))
    else:
        raise TypeError()


def getLogCategoryList(instrument_id: int) -> List:
    """Get a list of all log category for a specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int):
        return getData("instruments/{}/log_categories".format(instrument_id))
    else:
        raise TypeError()


def getLogCategory(instrument_id: int, log_category_id: int) -> Dict:
    """Get the specific log category (log_category_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_category_id (int): ID of the specific log category.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int) and isinstance(log_category_id, int):
        return getData("instruments/{}/log_categories/{}".format(
            instrument_id, log_category_id))
    else:
        raise TypeError()


def getFileAttachmentList(instrument_id: int, log_entry_id: int) -> List:
    """Get a list of file attachments for a specific log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return getData("instruments/{}/log_entries/{}/file_attachments".format(
            instrument_id, log_entry_id))
    else:
        raise TypeError()


def getFileAttachment(instrument_id: int, log_entry_id: int,
                      file_attachment_id: int) -> Dict:
    """Get a specific file attachment (file_attachment_id) for a log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.
        file_attachment_id (int): ID of the file attachment.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if (isinstance(instrument_id, int) and isinstance(log_entry_id, int) and
            isinstance(file_attachment_id, int)):
        return getData("instruments/{}/log_entries/{}/file_attachments/{}".format(
            instrument_id, log_entry_id, file_attachment_id))
    else:
        raise TypeError()


def getObjectAttachmentList(instrument_id: int, log_entry_id: int) -> List:
    """Get a list of object attachments for a specific log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.

    Returns:
        List: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return getData("instruments/{}/log_entries/{}/object_attachments".format(
            instrument_id, log_entry_id))
    else:
        raise TypeError()


def getObjectAttachment(instrument_id: int, log_entry_id: int, object_attachment_id: int) -> Dict:
    """Get a specific file attachment (file_attachment_id) for a log entry (log_entry_id) for an instrument (instrument_id).

    Args:
        instrument_id (int): ID of the instrument.
        log_entry_id (int): ID of the specific log entry.
        object_attachment_id (int): ID of the object attachment.

    Returns:
        Dict: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
    """
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int) and isinstance(object_attachment_id, int):
        return getData("instruments/{}/log_entries/{}/object_attachments/{}".format(
            instrument_id, log_entry_id, object_attachment_id))
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
