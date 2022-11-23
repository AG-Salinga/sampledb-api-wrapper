from __future__ import annotations

import base64
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

from requests import Response

from sampledbapi import SampleDBObject, get_data, post_data, users

__all__ = ["Instrument", "InstrumentLogCategory", "InstrumentLogEntry",
           "InstrumentLogFileAttachment", "InstrumentLogObjectAttachment",
           "get_list", "get"]


class Instrument(SampleDBObject):

    instrument_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_hidden: Optional[bool] = None
    instrument_scientists: Optional[List[users.User]] = None

    def __init__(self, d: Dict):
        """Initialize a new instrument from dictionary."""
        super().__init__(d)
        if "instrument_scientists" in d:
            self.instrument_scientists = [
                users.get(i) for i in d["instrument_scientists"]]

    def __repr__(self) -> str:
        return f"Instrument {self.instrument_id} ({self.name})"

    def get_log_entry_list(self) -> List[InstrumentLogEntry]:
        """Get a list of all log entries.

        Returns:
            List: List of :class:`~sampledbapi.instrument.InstrumentLogEntry`.
        """
        if self.instrument_id is not None:
            return [InstrumentLogEntry(self.instrument_id, log) for log in get_data(
                f"instruments/{self.instrument_id}/log_entries")]
        else:
            raise Exception('instrument_id can not be None')

    def get_log_entry(self, log_entry_id: int) -> InstrumentLogEntry:
        """Get the specific log entry (log_entry_id).

        Args:
            log_entry_id (int): ID of the specific log entry.

        Returns:
            InstrumentLogEntry: The requested
                :class:`~sampledbapi.instrument.InstrumentLogEntry`.
        """
        if isinstance(log_entry_id, int):
            if self.instrument_id is not None:
                return InstrumentLogEntry(self.instrument_id, get_data(
                    f"instruments/{self.instrument_id}/log_entries/{log_entry_id}"
                ))
            else:
                raise Exception('instrument_id can not be None')
        else:
            raise TypeError()

    def get_log_category_list(self) -> List[InstrumentLogCategory]:
        """Get a list of all log categories.

        Returns:
            List: List of :class:`~sampledbapi.instrument.InstrumentLogCategory`.
        """
        return [InstrumentLogCategory(c) for c in get_data(
            f"instruments/{self.instrument_id}/log_categories")]

    def get_log_category(self, log_category_id: int) -> InstrumentLogCategory:
        """Get a specific log category (log_category_id).

        Args:
            log_category_id (int): ID of the specific log category.

        Returns:
            InstrumentLogCategory: The requested
                :class:`~sampledbapi.instrument.InstrumentLogCategory`.
        """
        if isinstance(log_category_id, int):
            return InstrumentLogCategory(get_data(
                f"instruments/{self.instrument_id}/log_categories/" +
                f"{log_category_id}"))
        else:
            raise TypeError()

    def create_log_entry(self, content: str, category_ids: List = [],
                         file_attachments: List = [],
                         object_attachments: List = []) -> Response:
        """Create a log entry for an instrument (instrument_id) and optionally attach files and objects to it.

        Args:
            content (str): Log message.
            category_ids (list of ints): An optional list of category IDs for the log entry.
            file_attachments (list of strings): List of file paths to be read and attached to the log entry.
            object_attachments (list of integers): Object IDs to be attached to the log entry.

        Returns:
            HTTPResponse: `See here. <https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html#instrument-log-entries>`_
        """
        if (isinstance(content, str) and isinstance(category_ids, list) and
                isinstance(file_attachments, list) and
                isinstance(object_attachments, list)):
            data: Dict[str, Any] = {"content": content}

            def conv_file(path: str):
                with open(path, "rb") as f:
                    base64encoded = base64.b64encode(f.read())
                return {"file_name": os.path.basename(path),
                        "base64_content": base64encoded.decode()}

            if len(category_ids) > 0:
                data["category_ids"] = category_ids
            if len(file_attachments) > 0:
                data["file_attachments"] = [
                    conv_file(f) for f in file_attachments]
            if len(object_attachments) > 0:
                data["object_attachments"] = [
                    {"object_id": i} for i in object_attachments]

            return post_data(
                f"instruments/{self.instrument_id}/log_entries/", data)
        else:
            raise TypeError()


def get_list() -> List[Instrument]:
    """Get a list of all instruments.

    Returns:
        List: List of :class:`~sampledbapi.instrument.Instrument` objects.
    """
    return [Instrument(i) for i in get_data("instruments")]


def get(instrument_id: int) -> Instrument:
    """Get the specific instrument (instrument_id).

    Args:
        instrument_id (int): ID of the specific instrument.

    Returns:
        Instrument: The requested :class:`~sampledbapi.instrument.Instrument`.
    """
    if isinstance(instrument_id, int):
        return Instrument(get_data(f"instruments/{instrument_id}"))
    else:
        raise TypeError()


"""Instrument log entries"""


class InstrumentLogCategory(SampleDBObject):

    category_id: Optional[int] = None
    title: Optional[str] = None

    def __repr__(self) -> str:
        return f"InstrumentLogCategory {self.category_id} ({self.title})"


class InstrumentLogEntry(SampleDBObject):

    log_entry_id: Optional[int] = None
    instrument_id: Optional[int] = None
    utc_datetime: Optional[datetime] = None
    author: Optional[users.User] = None
    content: Optional[str] = None
    categories: Optional[List[InstrumentLogCategory]] = None

    def __init__(self, instrument_id: int, d: Dict):
        """Initialize a new instrument log entry from dictionary."""
        super().__init__(d)
        self.instrument_id = instrument_id
        if "categories" in d:
            self.categories = [
                InstrumentLogCategory(c) for c in d["categories"]]
        if "author" in d:
            self.author = users.get(d["author"])
        if "utc_datetime" in d:
            self.utc_datetime = datetime.strptime(
                d["utc_datetime"], '%Y-%m-%dT%H:%M:%S.%f')

    def __repr__(self) -> str:
        return f"InstrumentLogEntry {self.log_entry_id} " \
            + f"(created {self.utc_datetime})"

    def get_file_attachment_list(self) -> List[InstrumentLogFileAttachment]:
        """Get a list of file attachments.

        Returns:
            List: List of
                :class:`~sampledbapi.instrument.InstrumentLogFileAttachment`.
        """
        return [InstrumentLogFileAttachment(f) for f in get_data(
            f"instruments/{self.instrument_id}/log_entries/"
            f"{self.log_entry_id}/file_attachments")]

    def get_file_attachment(self, file_attachment_id: int
                            ) -> InstrumentLogFileAttachment:
        """Get a specific file attachment (file_attachment_id).

        Args:
            file_attachment_id (int): ID of the file attachment.

        Returns:
            InstrumentLogFileAttachment: The requested
                :class:`~sampledbapi.instrument.InstrumentLogFileAttachment`.
        """
        if isinstance(file_attachment_id, int):
            return InstrumentLogFileAttachment(get_data(
                f"instruments/{self.instrument_id}/log_entries/" +
                f"{self.log_entry_id}/file_attachments/{file_attachment_id}"))
        else:
            raise TypeError()

    def get_object_attachment_list(self) -> List[InstrumentLogObjectAttachment]:
        """Get a list of object attachments.

        Returns:
            List: List of
                :class:`~sampledbapi.instrument.InstrumentLogObjectAttachment`.
        """
        return [InstrumentLogObjectAttachment(o) for o in get_data(
            f"instruments/{self.instrument_id}/log_entries/"
            f"{self.log_entry_id}/object_attachments")]

    def get_object_attachment(self, object_attachment_id: int) -> InstrumentLogObjectAttachment:
        """Get a specific object attachment (object_attachment_id).

        Args:
            object_attachment_id (int): ID of the object attachment.

        Returns:
            InstrumentLogObjectAttachment: The requested
                :class:`~sampledbapi.instrument.InstrumentLogObjectAttachment`.
        """
        if isinstance(object_attachment_id, int):
            return InstrumentLogObjectAttachment(get_data(
                f"instruments/{self.instrument_id}/log_entries/"
                f"{self.log_entry_id}/object_attachments/"
                f"{object_attachment_id}"))
        else:
            raise TypeError()


class InstrumentLogFileAttachment(SampleDBObject):

    file_attachment_id: Optional[int] = None
    file_name: Optional[str] = None
    content: Optional[str] = None

    def __repr__(self) -> str:
        return f"InstrumentLogFileAttachment {self.file_attachment_id} " \
            + f"({self.file_name})"


class InstrumentLogObjectAttachment(SampleDBObject):

    object_attachment_id: Optional[int] = None
    object_id: Optional[int] = None

    def __repr__(self) -> str:
        return f"InstrumentLogObjectAttachment {self.object_attachment_id} " \
            + f"(for object {self.object_id})"
