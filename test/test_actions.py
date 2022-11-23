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
        
    def test_get_list(self, requests_mock):
        acts = actions.get_list()
        assert len(acts) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            actions.get('Test')
                
    def test_get_success(self, requests_mock):
        act = actions.get(1)
        assert act is not None
      
    def test_properties(self, requests_mock):
        act = actions.get(1)
        assert act.action_id == 1
        assert act.instrument_id == 2
        assert act.type == "Sample"
        assert act.type_id == 3
        assert act.name == "Create"
        assert act.description == "Create"
        assert act.is_hidden == False
        assert len(act.schema) > 0
        assert 'Action' in repr(act)