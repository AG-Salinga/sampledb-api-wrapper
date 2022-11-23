import pytest
from sampledbapi import objects, authenticate
from test import test_users, test_actions, test_objects

def mock_authenticate(requests_mock):
    requests_mock.get('http://128.176.208.107:8000/api/v1/users/me', text=test_users.mock_user())
    requests_mock.get("http://128.176.208.107:8000/api/v1/objects", text=test_objects.mock_objects())
    requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1", text=test_objects.mock_object())
    requests_mock.post("http://128.176.208.107:8000/api/v1/objects/", text=test_objects.mock_objects())
    requests_mock.put("http://128.176.208.107:8000/api/v1/objects/1/permissions/public")
    server_address = "http://128.176.208.107:8000"
    api_key = "Success"
    authenticate(server_address, api_key)

class TestAuthentication():
    
    def test_authentication_required_get(self):
        with pytest.raises(Exception):
            authenticate(None, None)
        with pytest.raises(Exception):
            objects.get_list()
            
    def test_authentication_required_post(self):
        with pytest.raises(Exception):
            authenticate(None, None)
        with pytest.raises(Exception):
            objects.create(1, {'name': 'Test'})
            
    def test_authentication_required_put(self, requests_mock):
        obj = objects.Object({})
        with pytest.raises(Exception):
            authenticate(None, None)
        with pytest.raises(Exception):
            obj.set_public(False) 
        
    def test_authenticate_fail(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/me", status_code=404)
        with pytest.raises(Exception):
            server_address = "http://128.176.208.107:8000"
            api_key = None
            authenticate(server_address, api_key)
        with pytest.raises(Exception):
            api_key = "Failure"
            authenticate(server_address, api_key)
        
    def test_authenticate_success(self, requests_mock):
        requests_mock.get('http://128.176.208.107:8000/api/v1/users/me', text=test_users.mock_user())
        server_address = "http://128.176.208.107:8000"
        api_key = "Success"
        authenticate(server_address, api_key)
        
    def test_json_fail(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/me", text="Fail")
        server_address = "http://128.176.208.107:8000"
        api_key = "Success"
        with pytest.raises(Exception):
            authenticate(server_address, api_key)