from typing import Dict, List

from sampledbapi import getData

__all__ = ["getList", "get", "getLogEntryList", "getLogEntry",
           "getLogCategoryList", "getLogCategory",
           "getFileAttachmentList", "getFileAttachment",
           "getObjectAttachmentList", "getObjectAttachment"]


def getList() -> List:
    """Get a list of all instruments."""
    return getData("instruments")


def get(instrument_id: int) -> Dict:
    """Get the specific instrument (instrument_id)."""
    if isinstance(instrument_id, int):
        return getData("instruments/{}".format(instrument_id))
    else:
        raise TypeError()


"""Instrument log entries"""


def getLogEntryList(instrument_id: int) -> List:
    """Get a list of all log entries for a specific instrument (instrument_id)."""
    if isinstance(instrument_id, int):
        return getData("instruments/{}/log_entries".format(instrument_id))
    else:
        raise TypeError()


def getLogEntry(instrument_id: int, log_entry_id: int) -> Dict:
    """Get the specific log entry (log_entry_id) for an instrument (instrument_id)."""
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return getData("instruments/{}/log_entries/{}".format(
            instrument_id, log_entry_id))
    else:
        raise TypeError()


def getLogCategoryList(instrument_id: int) -> List:
    """Get a list of all log category for a specific instrument (instrument_id)."""
    if isinstance(instrument_id, int):
        return getData("instruments/{}/log_categories".format(instrument_id))
    else:
        raise TypeError()


def getLogCategory(instrument_id: int, log_category_id: int) -> Dict:
    """Get the specific log categories (log_category_id) for an instrument (instrument_id)."""
    if isinstance(instrument_id, int) and isinstance(log_category_id, int):
        return getData("instruments/{}/log_categories/{}".format(
            instrument_id, log_category_id))
    else:
        raise TypeError()


def getFileAttachmentList(instrument_id: int, log_entry_id: int) -> List:
    """Get a list of file attachments for a specific log entry (log_entry_id) for an instrument (instrument_id)."""
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return getData("instruments/{}/log_entries/{}/file_attachments".format(
            instrument_id, log_entry_id))
    else:
        raise TypeError()


def getFileAttachment(instrument_id: int, log_entry_id: int, file_attachment_id: int) -> Dict:
    """Get a specific file attachment (file_attachment_id) for a log entry (log_entry_id) for an instrument (instrument_id)."""
    if (isinstance(instrument_id, int) and isinstance(log_entry_id, int) and
            isinstance(file_attachment_id, int)):
        return getData("instruments/{}/log_entries/{}/file_attachments/{}".format(
            instrument_id, log_entry_id, file_attachment_id))
    else:
        raise TypeError()


def getObjectAttachmentList(instrument_id: int, log_entry_id: int) -> List:
    """Get a list of object attachments for a specific log entry (log_entry_id) for an instrument (instrument_id)."""
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int):
        return getData("instruments/{}/log_entries/{}/object_attachments".format(
            instrument_id, log_entry_id))
    else:
        raise TypeError()


def getObjectAttachment(instrument_id: int, log_entry_id: int, object_attachment_id: int) -> Dict:
    """Get a specific file attachment (file_attachment_id) for a log entry (log_entry_id) for an instrument (instrument_id)."""
    if isinstance(instrument_id, int) and isinstance(log_entry_id, int) and isinstance(object_attachment_id, int):
        return getData("instruments/{}/log_entries/{}/object_attachments/{}".format(
            instrument_id, log_entry_id, object_attachment_id))
    else:
        raise TypeError()
