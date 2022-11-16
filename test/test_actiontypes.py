import pytest
from sampledbapi import actiontypes
from test import test_authentication

def mock_actiontype():
    return '''{
            "type_id": 1,
            "name": "Create Sample",
            "object_name": "Sample",
            "admin_only": false
        }'''

def mock_actiontypes():
    return f'[{mock_actiontype()},{mock_actiontype()},{mock_actiontype()}]'

class TestActiontypes():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/action_types", text=mock_actiontypes())
        requests_mock.get("http://128.176.208.107:8000/api/v1/action_types/1", text=mock_actiontype())
        test_authentication.mock_authenticate(requests_mock)
        
    def test_getList(self, requests_mock):
        locs = actiontypes.getList()
        assert len(locs) == 3
        
    def test_get(self, requests_mock):
        loc = actiontypes.get(1)
        assert loc != None
      
    def test_properties(self, requests_mock):
        loc = actiontypes.get(1)
        assert loc.type_id == 1
        assert loc.name == "Create Sample"
        assert loc.object_name == "Sample"
        assert loc.admin_only == False