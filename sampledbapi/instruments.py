from typing import Dict, List

from sampledbapi import getData

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
