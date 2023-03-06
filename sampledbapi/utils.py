from datetime import datetime
from sampledbapi import objects, SampleDBObject
from typing import Optional, Dict

class TimeSeries(SampleDBObject):
    data: Optional[float] = None
    units: Optional[str] = None
    
class Quantity(SampleDBObject):
    value: Optional[float] = None
    units: Optional[str] = None
    
def json2timeseries(data: dict) -> Optional[TimeSeries]:
    if '_type' not in data or data['_type'] != 'timeseries':
        return None
    return TimeSeries(data)
    
def timeseries2json(timeseries: TimeSeries) -> Dict:
    return {'_type': 'timeseries', 'data': str(timeseries.data), 'units': str(timeseries.units)} 
    
def json2objectreference(data: dict) -> Optional[int]:
    if '_type' not in data or data['_type'] != 'object_reference':
        return None
    return int(data['object_id'])
    
def objectreference2json(obj_id: int) -> Dict:
    return {'_type': 'object_reference', 'object_id': str(obj_id)}

def json2object(data: dict) -> Optional[objects.Object]:
    if '_type' not in data or data['_type'] != 'object_reference':
        return None
    return objects.get(int(data['object_id']))

def object2json(obj: objects.Object) -> Dict:
    return {'_type': 'object_reference', 'object_id': str(obj.object_id)}    

def json2bool(data: dict) -> Optional[bool]:
    if '_type' not in data or data['_type'] != 'bool':
        return None
    return data['value'] == 'True'

def bool2json(value: bool) -> Dict:
    return {'_type': 'bool', 'value': str(value)}
    
def json2quantity(data: dict) -> Optional[Quantity]:
    if '_type' not in data or data['_type'] != 'quantity':
        return None
    return Quantity(data)

def quantity2json(quantity: Quantity) -> Dict:
    return {'_type': 'quantity', 'value': str(quantity.value), 'units': str(quantity.units)}
    
def json2datetime(data: dict) -> Optional[datetime]:
    if '_type' not in data or data['_type'] != 'datetime':
        return None
    return datetime.strptime(data['utc_datetime'], '%Y-%m-%d %H:%M:%S')

def datetime2json(datetime: datetime) -> Dict:
    return {'_type': 'datetime', 'utc_datetime': datetime.strftime('%Y-%m-%d %H:%M:%S')}

def json2text(data: dict) -> Optional[str]:
    if '_type' not in data or data['_type'] != 'text':
        return None
    return data['text']

def text2json(text: str) -> Dict:
    return {'_type': 'text', 'text': text}
