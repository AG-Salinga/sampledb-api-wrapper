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
    
    def test_get_list(self):
        loctyps = locationtypes.get_list()
        assert len(loctyps) == 3
    
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            locationtypes.get('Test')
            
    def test_get_success(self):
        loctyp = locationtypes.get(1)
        assert loctyp is not None
        
    def test_properties(self):
        loctyp = locationtypes.get(1)
        assert loctyp.location_type_id == 1
        assert loctyp.name == 'Room'
        assert 'LocationType' in repr(loctyp)