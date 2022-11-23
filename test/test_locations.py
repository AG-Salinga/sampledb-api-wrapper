import pytest
from sampledbapi import locations
from test import test_authentication

def mock_location():
    return '''{
            "location_id": 1,
            "name": "IG1",
            "description": "IG1",
            "parent_location_id": 2,
            "type_id": 3,
            "is_hidden": false
        }'''

def mock_locations():
    return f'[{mock_location()},{mock_location()},{mock_location()}]'

class TestLocations():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/locations", text=mock_locations())
        requests_mock.get("http://128.176.208.107:8000/api/v1/locations/1", text=mock_location())
        test_authentication.mock_authenticate(requests_mock)
        
    def test_get_list(self, requests_mock):
        locs = locations.get_list()
        assert len(locs) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            locations.get('Test')
            
    def test_get_success(self, requests_mock):
        loc = locations.get(1)
        assert loc is not None
      
    def test_properties(self, requests_mock):
        loc = locations.get(1)
        assert loc.location_id == 1
        assert loc.name == "IG1"
        assert loc.description == "IG1"
        assert loc.parent_location_id == 2
        assert loc.type_id == 3
        assert loc.is_hidden == False
        assert 'Location' in repr(loc)