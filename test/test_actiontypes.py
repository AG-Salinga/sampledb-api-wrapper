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
        
    def test_get_list(self, requests_mock):
        acttyps = actiontypes.get_list()
        assert len(acttyps) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            actiontypes.get('Test')
        
    def test_get_success(self, requests_mock):
        acttyp = actiontypes.get(1)
        assert acttyp is not None
      
    def test_properties(self, requests_mock):
        acttyp = actiontypes.get(1)
        assert acttyp.type_id == 1
        assert acttyp.name == "Create Sample"
        assert acttyp.object_name == "Sample"
        assert acttyp.admin_only == False
        assert 'ActionType' in repr(acttyp)