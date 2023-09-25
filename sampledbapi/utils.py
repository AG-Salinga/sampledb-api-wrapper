from datetime import datetime
from typing import Optional, Dict

from .comm import SampleDBObject


class TimeSeries(SampleDBObject):
    data: Optional[str] = None
    units: Optional[str] = None


class Quantity(SampleDBObject):
    value: Optional[float] = None
    units: Optional[str] = None


def json2timeseries(data: Dict) -> Optional[TimeSeries]:
    if '_type' not in data or data['_type'] != 'timeseries':
        return None
    return TimeSeries(data)


def timeseries2json(timeseries: TimeSeries) -> Dict:
    return {'_type': 'timeseries', 'data': str(timeseries.data), 'units': str(timeseries.units)}


def json2objectreference(data: Dict) -> Optional[int]:
    if '_type' not in data or data['_type'] != 'object_reference':
        return None
    return int(data['object_id'])


def objectreference2json(obj_id: int) -> Dict:
    return {'_type': 'object_reference', 'object_id': obj_id}


def json2bool(data: Dict) -> Optional[bool]:
    if '_type' not in data or data['_type'] != 'bool':
        return None
    return data['value'] == 'True'


def bool2json(value: bool) -> Dict:
    return {'_type': 'bool', 'value': str(value)}


def json2quantity(data: Dict) -> Optional[Quantity]:
    if '_type' not in data or data['_type'] != 'quantity':
        return None
    return Quantity(data)


def quantity2json(quantity: Quantity) -> Dict:
    return {'_type': 'quantity', 'value': str(quantity.value), 'units': str(quantity.units)}


def json2datetime(data: Dict) -> Optional[datetime]:
    if '_type' not in data or data['_type'] != 'datetime':
        return None
    return str2datetime(data['utc_datetime'])


def datetime2json(datetime: datetime) -> Dict:
    return {'_type': 'datetime', 'utc_datetime': datetime.strftime('%Y-%m-%d %H:%M:%S')}


def json2text(data: Dict) -> Optional[str]:
    if '_type' not in data or data['_type'] != 'text':
        return None
    return data['text']


def text2json(text: str) -> Dict:
    return {'_type': 'text', 'text': text}


def str2datetime(data: str) -> datetime:
    return datetime.strptime(data, '%Y-%m-%d %H:%M:%S')


def file2json(file_id: int):
    return {'_type': 'file', 'file_id': file_id}


def convert_json(data: Dict):
    for key in data:
        if type(data[key]) is Dict:
            data[key] = convert_json(data[key])
        if key == '_type':
            if data[key] == 'text':
                data[key] = json2text(data[key])
            if data[key] == 'datetime':
                data[key] = json2datetime(data[key])
            if data[key] == 'quantity':
                data[key] = json2quantity(data[key])
            if data[key] == 'bool':
                data[key] = json2bool(data[key])
            if data[key] == 'object_reference':
                data[key] = json2objectreference(data[key])
            if data[key] == 'timeseries':
                data[key] = json2timeseries(data[key])
    return data
