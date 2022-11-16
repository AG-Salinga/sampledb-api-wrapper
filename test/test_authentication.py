import pytest
from sampledbapi import actions, authenticate
from test import test_actions

def mock_authenticate(requests_mock):
    requests_mock.get("http://128.176.208.107:8000/api/v1/actions", text=test_actions.mock_actions())
    server_address = "http://128.176.208.107:8000"
    api_key = "Success"
    authenticate(server_address, api_key)

class TestAuthentication():
    
    def test_AuthenticationRequired(self):
        with pytest.raises(Exception):
            actions.getList()
        
    def test_authenticate_fail(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/actions", status_code=404)
        with pytest.raises(Exception):
            server_address = "http://128.176.208.107:8000"
            api_key = "Failure"
            authenticate(server_address, api_key)
        
    def test_authenticate_success(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/actions", text=test_actions.mock_actions())
        server_address = "http://128.176.208.107:8000"
        api_key = "Success"
        authenticate(server_address, api_key)