import pytest
from sampledbapi import instruments
from test import test_authentication, test_users

def mock_instrument():
    return '''{
            "instrument_id": 1,
            "name": "MBE",
            "description": "Molecular-beam epitaxy",
            "is_hidden": false,
            "instrument_scientists": [1]
        }'''

def mock_instruments():
    return f'[{mock_instrument()},{mock_instrument()},{mock_instrument()}]'

class TestInstruments():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=test_users.mock_user())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments", text=mock_instruments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1", text=mock_instrument())
        test_authentication.mock_authenticate(requests_mock)
        
    def test_getList(self, requests_mock):
        locs = instruments.getList()
        assert len(locs) == 3
        
    def test_get(self, requests_mock):
        loc = instruments.get(1)
        assert loc != None
      
    def test_properties(self, requests_mock):
        loc = instruments.get(1)
        assert loc.instrument_id == 1
        assert loc.name == "MBE"
        assert loc.description == "Molecular-beam epitaxy"
        assert loc.is_hidden == False
        assert loc.instrument_scientists != None