import pytest
from sampledbapi import users
from test import test_authentication

def mock_user():
    return '''{
            "user_id": 1,
            "name": "Nils Weber",
            "orcid": "12345",
            "affiliation": "WWU Münster"
        }'''

def mock_users():
    return f'[{mock_user()},{mock_user()},{mock_user()}]'

class TestUsers():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users", text=mock_users())
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=mock_user())
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/me", text=mock_user())
        test_authentication.mock_authenticate(requests_mock)
        
    def test_get_list(self, requests_mock):
        usrs = users.get_list()
        assert len(usrs) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            users.get('Test')
            
    def test_get_success(self, requests_mock):
        usr = users.get(1)
        assert usr != None
      
    def test_properties(self, requests_mock):
        usr = users.get(1)
        assert usr.user_id == 1
        assert usr.name == "Nils Weber"
        assert usr.orcid == "12345"
        assert usr.affiliation == "WWU Münster"
        assert 'User' in repr(usr)
        
    def test_get_current(self, requests_mock):
        usr = users.get_current()
        assert usr != None