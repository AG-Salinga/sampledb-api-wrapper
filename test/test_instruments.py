import pytest
import tempfile
from sampledbapi import instruments
from test import test_authentication, test_users

def mock_instrument():
    return '''{
            "instrument_id": 1,
            "name": "MBE",
            "description": "Molecular-beam epitaxy",
            "is_hidden": false,
            "instrument_scientists": [1]
        }'''

def mock_instruments():
    return f'[{mock_instrument()},{mock_instrument()},{mock_instrument()}]'

def mock_logEntry():
    return '''{
            "log_entry_id": 1,
            "instrument_id": 1,
            "utc_datetime": "2022-11-21T09:39:08.470159",
            "author": 1,
            "content": "Dies ist ein Test-Text",
            "categories": ["1"]
        }'''
    
    #"categories": [1] ?

def mock_logEntries():
    return f'[{mock_logEntry()},{mock_logEntry()},{mock_logEntry()}]'

def mock_logCategory():
    return '''{
            "category_id": 1,
            "title": "TestCategory"
        }'''

def mock_logCategories():
    return f'[{mock_logCategory()},{mock_logCategory()},{mock_logCategory()}]'

def mock_fileAttachment():
    return '''{
            "file_attachment_id": 1,
            "file_name": "TestName",
            "content": "TestContent"
        }'''
    
def mock_fileAttachments():
    return f'[{mock_fileAttachment()},{mock_fileAttachment()},{mock_fileAttachment()}]'
    
def mock_objectAttachment():
    return '''{
            "object_attachment_id": 1,
            "object_id": 1
        }'''
    
def mock_objectAttachments():
    return f'[{mock_objectAttachment()},{mock_objectAttachment()},{mock_objectAttachment()}]'

class TestInstruments():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=test_users.mock_user())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments", text=mock_instruments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1", text=mock_instrument())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries", text=mock_logEntries())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1", text=mock_logEntry())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_categories", text=mock_logCategories())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_categories/1", text=mock_logCategory())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/file_attachments", text=mock_fileAttachments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/file_attachments/1", text=mock_fileAttachment())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/object_attachments", text=mock_objectAttachments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/object_attachments/1", text=mock_objectAttachment())
        requests_mock.post("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/")

        test_authentication.mock_authenticate(requests_mock)
     
    def test_getList(self, requests_mock):
        insts = instruments.getList()
        assert len(insts) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get('Test')
        
    def test_get_success(self, requests_mock):
        inst = instruments.get(1)
        assert inst != None
      
    def test_properties(self, requests_mock):
        inst = instruments.get(1)
        assert inst.instrument_id == 1
        assert inst.name == "MBE"
        assert inst.description == "Molecular-beam epitaxy"
        assert inst.is_hidden == False
        assert inst.instrument_scientists != None
        assert 'Instrument' in repr(inst)
        
    def test_getLogEntryList(self, requests_mock):
        logs = instruments.get(1).getLogEntryList()
        assert len(logs) == 3
        
    def test_getLogEntry_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).getLogEntry('Test')
        
    def test_getLogEntry_success(self, requests_mock):
        log = instruments.get(1).getLogEntry(1)
        assert log != None
        
    def test_logEntry_properties(self, requests_mock):
        log = instruments.get(1).getLogEntry(1)
        assert log.log_entry_id == 1
        assert log.instrument_id == 1
        assert log.utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f') == '2022-11-21T09:39:08.470159'
        assert log.author != None
        assert log.content == 'Dies ist ein Test-Text'
        assert len(log.categories) > 0
        assert 'InstrumentLogEntry' in repr(log)
        
    def test_getLogCategoryList(self, requests_mock):
        logCats = instruments.get(1).getLogCategoryList()
        assert len(logCats) == 3
        
    def test_getLogCategory_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).getLogCategory('Test')
            
    def test_getLogCategory_success(self, requests_mock):
        logCat = instruments.get(1).getLogCategory(1)
        assert logCat != None
        
    def test_getLogCategory_properties(self, requests_mock):
        logCat = instruments.get(1).getLogCategory(1)
        assert logCat.category_id == 1
        assert logCat.title == 'TestCategory'
        assert 'InstrumentLogCategory' in repr(logCat)
        
    def test_createLogEntry_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).createLogEntry(1, [], [], [])
        
    def test_createLogEntry_success(self, requests_mock):
        new_file, filename = tempfile.mkstemp()
        instruments.get(1).createLogEntry('TestContent', [1], [filename], [1])
    
    def test_getFileAttachmentList(self, requests_mock):
        fileAtts = instruments.get(1).getLogEntry(1).getFileAttachmentList()
        assert len(fileAtts) == 3
        
    def test_getFileAttachment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).getLogEntry(1).getFileAttachment('Test')
        
    def test_getFileAttachment_success(self, requests_mock):
        fileAtt = instruments.get(1).getLogEntry(1).getFileAttachment(1)
        assert fileAtt != None
        
    def test_getFileAttachment_properties(self, requests_mock):
        fileAtt = instruments.get(1).getLogEntry(1).getFileAttachment(1)
        assert fileAtt.file_attachment_id == 1
        assert fileAtt.file_name == 'TestName'
        assert fileAtt.content == 'TestContent'
        assert 'InstrumentLogFileAttachment' in repr(fileAtt)
    
    def test_getObjectAttachmentList(self, requests_mock):
        objAtts = instruments.get(1).getLogEntry(1).getObjectAttachmentList()
        assert len(objAtts) == 3
        
    def test_getObjectAttachment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).getLogEntry(1).getObjectAttachment('Test')
            
    def test_getObjectAttachment_success(self, requests_mock):
        objAtt = instruments.get(1).getLogEntry(1).getObjectAttachment(1)
        assert objAtt != None
        
    def test_getObjectAttachment_properties(self, requests_mock):
        objAtt = instruments.get(1).getLogEntry(1).getObjectAttachment(1)
        assert objAtt.object_attachment_id == 1
        assert objAtt.object_id == 1
        assert 'InstrumentLogObjectAttachment' in repr(objAtt)