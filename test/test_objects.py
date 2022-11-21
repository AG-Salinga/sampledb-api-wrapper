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

def mock_locationOccurence():
    return '''{
            "object_id": 1,
            "location": 1,
            "responsible_user": 1,
            "user": 1,
            "description": "TestDescription",
            "utc_datetime": "2022-11-21T09:39:08.470159"
        }'''
    
def mock_locationOccurences():
    return f'[{mock_locationOccurence()},{mock_locationOccurence()},{mock_locationOccurence()}]'

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
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/locations", text=mock_locationOccurences())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/locations/1", text=mock_locationOccurence())
        requests_mock.get("http://128.176.208.107:8000/api/v1/locations/1", text=test_locations.mock_location())
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=test_users.mock_user())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/files", text=mock_files())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/files/1", text=mock_file())
        requests_mock.post("http://128.176.208.107:8000/api/v1/objects/1/files/")
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/comments", text=mock_comments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/objects/1/comments/1", text=mock_comment())
        requests_mock.post("http://128.176.208.107:8000/api/v1/objects/1/comments/")
        
        test_authentication.mock_authenticate(requests_mock)
       
    def test_getList_default(self, requests_mock):
        objs = objects.getList()
        assert len(objs) == 3
        
    def test_getList_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.getList(q=1)
        
    def test_getList_success(self, requests_mock):
        objs = objects.getList(q='Test', action_id=1, action_type='Create', limit=3, offset=3, name_only=True)
        assert len(objs) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get('Test')
            
    def test_get_success(self, requests_mock):
        obj = objects.get(1)
        assert obj != None
      
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
        
    def test_getVersion_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getVersion('Test')
        
    def test_getVersion_success(self, requests_mock):
        obj = objects.get(1).getVersion(1)
        assert obj != None 
        
    def test_update_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).update('Test')
        
    def test_update_success(self, requests_mock):
        objects.get(1).update({"title": "Basic Sample Information"})
        
    def test_getPublic(self, requests_mock):
        assert objects.get(1).getPublic()
        
    def test_setPublic_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).setPublic('Test')
        
    def test_setPublic_success(self, requests_mock):
        objects.get(1).setPublic(False) 
        
    def test_getAllUsersPermissions(self, requests_mock):
        perm = objects.get(1).getAllUsersPermissions()
        assert type(perm) == dict
        assert len(perm) == 3
        
    def test_getUserPermissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getUserPermissions('Test')
        
    def test_getUserPermissions_success(self, requests_mock):
        perm = objects.get(1).getUserPermissions(1)     
        assert type(perm) == str
        assert perm != None
        
    def test_setUserPermissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).setUserPermissions('Test', 'TestPerm')
        
    def test_setUserPermissions_success(self, requests_mock):
        objects.get(1).setUserPermissions(1, 'TestPerm')    
        
    def test_getAllGroupPermissions(self, requests_mock):
        perm = objects.get(1).getAllGroupsPermissions()
        assert type(perm) == dict
        assert len(perm) == 3
        
    def test_getGroupPermissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getGroupPermissions('Test')
        
    def test_getGroupPermissions_success(self, requests_mock):
        perm = objects.get(1).getGroupPermissions(1)     
        assert type(perm) == str
        assert perm != None
        
    def test_setGroupPermissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).setGroupPermissions('Test', 'TestPerm')
        
    def test_setGroupPermissions_success(self, requests_mock):
        objects.get(1).setGroupPermissions(1, 'TestPerm')   
    
    def test_getAllProjectGroupPermissions(self, requests_mock):
        perm = objects.get(1).getAllProjectGroupsPermissions()
        assert type(perm) == dict
        assert len(perm) == 3
        
    def test_getProjectGroupPermissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getProjectGroupPermissions('Test')
        
    def test_getProjectGroupPermissions_success(self, requests_mock):
        perm = objects.get(1).getProjectGroupPermissions(1)     
        assert type(perm) == str
        assert perm != None
        
    def test_setProjectGroupPermissions_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).setProjectGroupPermissions('Test', 'TestPerm')
        
    def test_setProjectGroupPermissions_success(self, requests_mock):
        objects.get(1).setProjectGroupPermissions(1, 'TestPerm')  
    
    def test_getLocationOccurences(self, requests_mock):
        locOccs = objects.get(1).getLocationOccurences()
        assert len(locOccs) == 3
        
    def test_getLocationOccurence_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getLocationOccurence('Test')
            
    def test_getLocationOccurence_success(self, requests_mock):
        locOcc = objects.get(1).getLocationOccurence(1)
        assert locOcc is not None
        
    def test_getLocationOccurence_properties(self, requests_mock):
        locOcc = objects.get(1).getLocationOccurence(1)
        assert locOcc.object_id == 1
        assert locOcc.location is not None
        assert locOcc.responsible_user is not None
        assert locOcc.user is not None
        assert locOcc.description == 'TestDescription'
        assert locOcc.utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f') == '2022-11-21T09:39:08.470159'
        assert 'LocationOccurence of object' in repr(locOcc)
    
    def test_getFileList(self, requests_mock):
        files = objects.get(1).getFileList()
        assert len(files) == 3
    
    def test_getFile_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getFile('Test')
        
    def test_getFile_success(self, requests_mock):
        file = objects.get(1).getFile(1)
        assert file != None
        
    def test_getFile_properties(self, requests_mock):
        file = objects.get(1).getFile(1)
        assert file.object_id == 1
        assert file.file_id == 1
        assert file.storage == 'database'
        assert file.original_file_name == 'Test.txt'
        assert file.base64_content == 'Test64'
        assert 'File' in repr(file)
    
    def test_uploadFile_default(self, requests_mock):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.close()
        objects.get(1).uploadFile(f.name)
        
    def test_uploadFile_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).uploadFile(1)
        
    def test_uploadFile_success(self, requests_mock):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.close()
        objects.get(1).uploadFile(f.name, 'Testfile')
    
    def test_uploadFileRaw_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).uploadFileRaw(1, io.BytesIO(b"some initial binary data: \x00\x01"))
        
    def test_uploadFileRaw_success(self, requests_mock):
        objects.get(1).uploadFileRaw('TestFile', io.BytesIO(b"some initial binary data: \x00\x01"))
    
    def test_postLink_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).postLink(1)
        
    def test_postLink_success(self, requests_mock):
        objects.get(1).postLink('http://128.176.208.107:8000/instruments/1#log_entry-1')
    
    def test_getCommentList(self, requests_mock):
        coms = objects.get(1).getCommentList()
        assert len(coms) == 3
        
    def test_getComment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).getComment('Test')
        
    def test_getComment_success(self, requests_mock):
        com = objects.get(1).getComment(1)
        assert com != None
    
    def test_getComment_properties(self, requests_mock):
        com = objects.get(1).getComment(1)
        assert com.object_id == 1
        assert com.user_id == 1
        assert com.comment_id == 1
        assert com.content == 'TestContent'
        assert com.utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f') == '2022-11-21T09:39:08.470159'
        assert 'Comment on object' in str(com)
      
    def test_postComment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            objects.get(1).postComment(1)
        
    def test_postComment_success(self, requests_mock):
        objects.get(1).postComment('TestComment')
    