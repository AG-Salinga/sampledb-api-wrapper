import pytest
import io
import tempfile
from sampledbapi import objects
from test import test_authentication, test_users, test_locations

def mock_object():
    return '''{
            "object_id": 1,
            "version_id": 1,
            "action_id": 1,
            "schema": {"title": "Basic Sample Information"},
            "data": {"title": "Basic Sample Information"}
        }'''

def mock_objects():
    return f'[{mock_object()},{mock_object()},{mock_object()}]'

def mock_permission():
    return '"TestPerm"'
    
def mock_permissions():
    return '{"1": "TestPerm", "2": "TestPerm", "3": "TestPerm"}'

def mock_location_occurence():
    return '''{
            "object_id": 1,
            "location": 1,
            "responsible_user": 1,
            "user": 1,
            "description": "TestDescription",
            "utc_datetime": "2022-11-21T09:39:08.470159"
        }'''
    
def mock_location_occurences():
    return f'[{mock_location_occurence()},{mock_location_occurence()},{mock_location_occurence()}]'

def mock_file():
    return '''{
            "object_id": 1,
            "file_id": 1,
            "storage": "database",
            "original_file_name": "Test.txt",
            "base64_content": "Test64"
        }'''

def mock_files():
    return f'[{mock_file()},{mock_file()},{mock_file()}]'
    
def mock_comment():
    return '''{
            "object_id": 1,
            "user_id": 1,
            "comment_id": 1,
            "content": "TestContent",
            "utc_datetime": "2022-11-21T09:39:08.470159"
        }'''
    
def mock_comments():
    return f'[{mock_comment()},{mock_comment()},{mock_comment()}]'

class TestObjects():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects", text=mock_objects())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1", text=mock_object())
        requests_mock.post("http://128.176.208.107:8000/api/v1/objects/", text=mock_objects())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/versions/1", text=mock_object())
        requests_mock.post("http://128.176.208.107:8000/api/v1/objects/1/versions/")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/public", text=mock_permissions())
        requests_mock.put("http://128.176.208.107:8000/api/v1/objects/1/permissions/public")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/users", text=mock_permissions())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/users/1", text=mock_permission())
        requests_mock.put("http://128.176.208.107:8000/api/v1/objects/1/permissions/users/1")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/groups", text=mock_permissions())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/groups/1", text=mock_permission())
        requests_mock.put("http://128.176.208.107:8000/api/v1/objects/1/permissions/groups/1")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/projects", text=mock_permissions())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/permissions/projects/1", text=mock_permission())
        requests_mock.put("http://128.176.208.107:8000/api/v1/objects/1/permissions/projects/1")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/locations", text=mock_location_occurences())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/locations/1", text=mock_location_occurence())
        requests_mock.get("http://128.176.208.107:8000/api/v1/locations/1", text=test_locations.mock_location())
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=test_users.mock_user())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/files", text=mock_files())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/files/1", text=mock_file())
        requests_mock.post("http://128.176.208.107:8000/api/v1/objects/1/files/")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/comments", text=mock_comments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/comments/1", text=mock_comment())
        requests_mock.post("http://128.176.208.107:8000/api/v1/objects/1/comments/")
        
        test_authentication.mock_authenticate(requests_mock)
       
    def test_get_list_default(self, requests_mock):
        objs = objects.get_list()
        assert len(objs) == 3
        
    def test_get_list_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get_list(q=1)
        
    def test_get_list_success(self, requests_mock):
        objs = objects.get_list(q='Test', action_id=1, action_type='Create', limit=3, offset=3, name_only=True)
        assert len(objs) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get('Test')
            
    def test_get_success(self, requests_mock):
        obj = objects.get(1)
        assert obj is not None
      
    def test_properties(self, requests_mock):
        obj = objects.get(1)
        assert obj.object_id == 1
        assert obj.version_id == 1
        assert obj.action_id == 1
        assert len(obj.schema) > 0
        assert len(obj.data) > 0
        assert 'Object' in repr(obj)
        
    def test_create_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.create('Test', {'name': 'Test'})
        
    def test_create_success(self, requests_mock):
        objects.create(1, {'name': 'Test'})
        
    def test_get_version_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_version('Test')
        
    def test_get_version_success(self, requests_mock):
        obj = objects.get(1).get_version(1)
        assert obj is not None 
        
    def test_update_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).update('Test')
        
    def test_update_success(self, requests_mock):
        objects.get(1).update({"title": "Basic Sample Information"})
        
    def test_get_public(self, requests_mock):
        assert objects.get(1).get_public()
        
    def test_set_public_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).set_public('Test')
        
    def test_set_public_success(self, requests_mock):
        objects.get(1).set_public(False) 
        
    def test_get_all_user_permissions(self, requests_mock):
        perm = objects.get(1).get_all_user_permissions()
        assert type(perm) == dict
        assert len(perm) == 3
        
    def test_get_user_permissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_user_permissions('Test')
        
    def test_get_user_permissions_success(self, requests_mock):
        perm = objects.get(1).get_user_permissions(1)     
        assert type(perm) == str
        assert perm is not None
        
    def test_set_user_permissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).set_user_permissions('Test', 'TestPerm')
        
    def test_set_user_permissions_success(self, requests_mock):
        objects.get(1).set_user_permissions(1, 'TestPerm')    
        
    def test_get_all_group_permissions(self, requests_mock):
        perm = objects.get(1).get_all_group_permissions()
        assert type(perm) == dict
        assert len(perm) == 3
        
    def test_get_group_permissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_group_permissions('Test')
        
    def test_get_group_permissions_success(self, requests_mock):
        perm = objects.get(1).get_group_permissions(1)     
        assert type(perm) == str
        assert perm is not None
        
    def test_set_group_permissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).set_group_permissions('Test', 'TestPerm')
        
    def test_set_group_permissions_success(self, requests_mock):
        objects.get(1).set_group_permissions(1, 'TestPerm')   
    
    def test_get_all_project_group_permissions(self, requests_mock):
        perm = objects.get(1).get_all_project_group_permissions()
        assert type(perm) == dict
        assert len(perm) == 3
        
    def test_get_project_group_permissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_project_group_permissions('Test')
        
    def test_get_project_group_permissions_success(self, requests_mock):
        perm = objects.get(1).get_project_group_permissions(1)     
        assert type(perm) == str
        assert perm is not None
        
    def test_set_project_group_permissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).set_project_group_permissions('Test', 'TestPerm')
        
    def test_set_project_group_permissions_success(self, requests_mock):
        objects.get(1).set_project_group_permissions(1, 'TestPerm')  
    
    def test_get_location_occurences(self, requests_mock):
        locOccs = objects.get(1).get_location_occurences()
        assert len(locOccs) == 3
        
    def test_get_location_occurence_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_location_occurence('Test')
            
    def test_get_location_occurence_success(self, requests_mock):
        locOcc = objects.get(1).get_location_occurence(1)
        assert locOcc is not None
        
    def test_get_location_occurence_properties(self, requests_mock):
        locOcc = objects.get(1).get_location_occurence(1)
        assert locOcc.object_id == 1
        assert locOcc.location is not None
        assert locOcc.responsible_user is not None
        assert locOcc.user is not None
        assert locOcc.description == 'TestDescription'
        assert locOcc.utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f') == '2022-11-21T09:39:08.470159'
        assert 'LocationOccurence of object' in repr(locOcc)
    
    def test_get_file_list(self, requests_mock):
        files = objects.get(1).get_file_list()
        assert len(files) == 3
    
    def test_get_file_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_file('Test')
        
    def test_get_file_success(self, requests_mock):
        file = objects.get(1).get_file(1)
        assert file is not None
        
    def test_get_file_properties(self, requests_mock):
        file = objects.get(1).get_file(1)
        assert file.object_id == 1
        assert file.file_id == 1
        assert file.storage == 'database'
        assert file.original_file_name == 'Test.txt'
        assert file.base64_content == 'Test64'
        assert 'File' in repr(file)
    
    def test_upload_file_default(self, requests_mock):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.close()
        objects.get(1).upload_file(f.name)
        
    def test_upload_file_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).upload_file(1)
        
    def test_upload_file_success(self, requests_mock):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.close()
        objects.get(1).upload_file(f.name, 'Testfile')
    
    def test_upload_file_raw_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).upload_file_raw(1, io.BytesIO(b"some initial binary data: \x00\x01"))
        
    def test_upload_file_raw_success(self, requests_mock):
        objects.get(1).upload_file_raw('TestFile', io.BytesIO(b"some initial binary data: \x00\x01"))
    
    def test_post_link_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).post_link(1)
        
    def test_post_link_success(self, requests_mock):
        objects.get(1).post_link('http://128.176.208.107:8000/instruments/1#log_entry-1')
    
    def test_get_comment_list(self, requests_mock):
        coms = objects.get(1).get_comment_list()
        assert len(coms) == 3
        
    def test_get_comment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).get_comment('Test')
        
    def test_get_comment_success(self, requests_mock):
        com = objects.get(1).get_comment(1)
        assert com is not None
    
    def test_get_comment_properties(self, requests_mock):
        com = objects.get(1).get_comment(1)
        assert com.object_id == 1
        assert com.user_id == 1
        assert com.comment_id == 1
        assert com.content == 'TestContent'
        assert com.utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f') == '2022-11-21T09:39:08.470159'
        assert 'Comment on object' in str(com)
      
    def test_post_comment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).post_comment(1)
        
    def test_postComment_success(self, requests_mock):
        objects.get(1).post_comment('TestComment')
    