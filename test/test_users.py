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

class TestInstruments():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users", text=mock_users())
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=mock_user())
        test_authentication.mock_authenticate(requests_mock)
        
    def test_getList(self, requests_mock):
        locs = users.getList()
        assert len(locs) == 3
        
    def test_get(self, requests_mock):
        loc = users.get(1)
        assert loc != None
      
    def test_properties(self, requests_mock):
        loc = users.get(1)
        assert loc.user_id == 1
        assert loc.name == "Nils Weber"
        assert loc.orcid == "12345"
        assert loc.affiliation == "WWU Münster"