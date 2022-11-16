import pytest
from sampledbapi import locationtypes
from test import test_authentication

def mock_locationtype():
    return '''{
            "location_type_id": 1,
            "name": "Room"
        }'''

def mock_locationtypes():
    return f'[{mock_locationtype()},{mock_locationtype()},{mock_locationtype()}]'

class TestLocationTypes():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/location_types", text=mock_locationtypes())
        requests_mock.get("http://128.176.208.107:8000/api/v1/location_types/1", text=mock_locationtype())
        test_authentication.mock_authenticate(requests_mock)
    
    def test_getList(self):
        locs = locationtypes.getList()
        assert len(locs) == 3
        
    def test_get(self):
        loc = locationtypes.get(1)
        assert loc != None
        
    def test_properties(self):
        loc = locationtypes.get(1)
        assert loc.location_type_id == 1
        assert loc.name == 'Room'