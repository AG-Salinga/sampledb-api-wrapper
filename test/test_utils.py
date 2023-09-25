from sampledbapi. utils import *
from test import test_authentication, test_users

class TestUtils():
    
    def test_json2timeseries_fail(self):
        assert json2timeseries('') is None
        assert json2timeseries({'_type': 'test'}) is None
    
    def test_json2timeseries2json(self):
        json = {'_type': 'timeseries', 'data': '"2023-12-22 11:11:11.111111",20.0,293.15\n"2023-12-22 12:11:11.111111",21.0,294.15', 'units': 'DegC'}
        timeseries = json2timeseries(json)
        json2 = timeseries2json(timeseries)
        assert json == json2
    
    def test_json2objectreference_fail(self):
        assert json2objectreference('') is None
        assert json2objectreference({'_type': 'test'}) is None
        
    def test_json2objectreference2json(self):
        json = {'_type': 'object_reference', 'object_id': 1}
        objectreference = json2objectreference(json)
        json2 = objectreference2json(objectreference)
        assert json == json2
        
    def test_json2bool_fail(self):
        assert json2bool('') is None
        assert json2bool({'_type': 'test'}) is None
        
    def test_json2bool2json(self):
        json = {'_type': 'bool', 'value': 'True'}
        bol = json2bool(json)
        json2 = bool2json(bol)
        assert json == json2
        
    def test_json2quantity_fail(self):
        assert json2quantity('') is None
        assert json2quantity({'_type': 'test'}) is None
        
    def test_json2quantity2json(self):
        json = {'_type': 'quantity', 'value': '2.46', 'units': 'DegC'}
        quantity = json2quantity(json)
        json2 = quantity2json(quantity)
        assert json == json2
        
    def test_json2datetime_fail(self):
        assert json2datetime('') is None
        assert json2datetime({'_type': 'test'}) is None
        
    def test_json2datetime2json(self):
        json = {'_type': 'datetime', 'utc_datetime': '2020-01-03 11:11:11'}
        datetime = json2datetime(json)
        json2 = datetime2json(datetime)
        assert json == json2
        
    def test_json2text_fail(self):
        assert json2text('') is None
        assert json2text({'_type': 'test'}) is None
        
    def test_json2text2json(self):
        json = {'_type': 'text', 'text': 'Test'}
        text = json2text(json)
        json2 = text2json(text)
        assert json == json2
