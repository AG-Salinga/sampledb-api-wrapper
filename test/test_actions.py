import pytest
from sampledbapi import actions
from test import test_authentication

def mock_action():
    return '''{
            "action_id": 1,
            "instrument_id": 2,
            "type": "Sample",
            "type_id": 3,
            "name": "Create",
            "description": "Create",
            "is_hidden": false,
            "schema": {"title": "Basic Sample Information"}
        }'''

def mock_actions():
    return f'[{mock_action()},{mock_action()},{mock_action()}]'

class TestActions():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/actions", text=mock_actions())
        requests_mock.get("http://128.176.208.107:8000/api/v1/actions/1", text=mock_action())
        test_authentication.mock_authenticate(requests_mock)
        
    def test_getList(self, requests_mock):
        locs = actions.getList()
        assert len(locs) == 3
        
    def test_get(self, requests_mock):
        loc = actions.get(1)
        assert loc != None
      
    def test_properties(self, requests_mock):
        loc = actions.get(1)
        assert loc.action_id == 1
        assert loc.instrument_id == 2
        assert loc.type == "Sample"
        assert loc.type_id == 3
        assert loc.name == "Create"
        assert loc.description == "Create"
        assert loc.is_hidden == False
        assert len(loc.schema) > 0