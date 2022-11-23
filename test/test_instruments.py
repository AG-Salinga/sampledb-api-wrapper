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

def mock_log_entry():
    return '''{
            "log_entry_id": 1,
            "instrument_id": 1,
            "utc_datetime": "2022-11-21T09:39:08.470159",
            "author": 1,
            "content": "Dies ist ein Test-Text",
            "categories": ["1"]
        }'''
    
    #"categories": [1] ?

def mock_log_entries():
    return f'[{mock_log_entry()},{mock_log_entry()},{mock_log_entry()}]'

def mock_log_category():
    return '''{
            "category_id": 1,
            "title": "TestCategory"
        }'''

def mock_log_categories():
    return f'[{mock_log_category()},{mock_log_category()},{mock_log_category()}]'

def mock_file_attachment():
    return '''{
            "file_attachment_id": 1,
            "file_name": "TestName",
            "content": "TestContent"
        }'''
    
def mock_file_attachments():
    return f'[{mock_file_attachment()},{mock_file_attachment()},{mock_file_attachment()}]'
    
def mock_object_attachment():
    return '''{
            "object_attachment_id": 1,
            "object_id": 1
        }'''
    
def mock_object_attachments():
    return f'[{mock_object_attachment()},{mock_object_attachment()},{mock_object_attachment()}]'

class TestInstruments():
    
    @pytest.fixture(autouse=True)
    def test_init(self, requests_mock):
        requests_mock.get("http://128.176.208.107:8000/api/v1/users/1", text=test_users.mock_user())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments", text=mock_instruments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1", text=mock_instrument())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries", text=mock_log_entries())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1", text=mock_log_entry())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_categories", text=mock_log_categories())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_categories/1", text=mock_log_category())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/file_attachments", text=mock_file_attachments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/file_attachments/1", text=mock_file_attachment())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/object_attachments", text=mock_object_attachments())
        requests_mock.get("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/1/object_attachments/1", text=mock_object_attachment())
        requests_mock.post("http://128.176.208.107:8000/api/v1/instruments/1/log_entries/")

        test_authentication.mock_authenticate(requests_mock)
     
    def test_get_list(self, requests_mock):
        insts = instruments.get_list()
        assert len(insts) == 3
        
    def test_get_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get('Test')
        
    def test_get_success(self, requests_mock):
        inst = instruments.get(1)
        assert inst is not None
      
    def test_properties(self, requests_mock):
        inst = instruments.get(1)
        assert inst.instrument_id == 1
        assert inst.name == "MBE"
        assert inst.description == "Molecular-beam epitaxy"
        assert inst.is_hidden == False
        assert inst.instrument_scientists is not None
        assert 'Instrument' in repr(inst)
        
    def test_get_log_entry_list(self, requests_mock):
        logs = instruments.get(1).get_log_entry_list()
        assert len(logs) == 3
        
    def test_get_log_entry_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).get_log_entry('Test')
        
    def test_get_log_entry_success(self, requests_mock):
        log = instruments.get(1).get_log_entry(1)
        assert log is not None
        
    def test_log_entry_properties(self, requests_mock):
        log = instruments.get(1).get_log_entry(1)
        assert log.log_entry_id == 1
        assert log.instrument_id == 1
        assert log.utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f') == '2022-11-21T09:39:08.470159'
        assert log.author is not None
        assert log.content == 'Dies ist ein Test-Text'
        assert len(log.categories) > 0
        assert 'InstrumentLogEntry' in repr(log)
        
    def test_get_log_category_list(self, requests_mock):
        logCats = instruments.get(1).get_log_category_list()
        assert len(logCats) == 3
        
    def test_get_log_category_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).get_log_category('Test')
            
    def test_get_log_category_success(self, requests_mock):
        logCat = instruments.get(1).get_log_category(1)
        assert logCat is not None
        
    def test_get_log_category_properties(self, requests_mock):
        logCat = instruments.get(1).get_log_category(1)
        assert logCat.category_id == 1
        assert logCat.title == 'TestCategory'
        assert 'InstrumentLogCategory' in repr(logCat)
        
    def test_create_log_entry_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).create_log_entry(1, [], [], [])
        
    def test_create_log_entry_success(self, requests_mock):
        new_file, filename = tempfile.mkstemp()
        instruments.get(1).create_log_entry('TestContent', [1], [filename], [1])
    
    def test_get_file_attachment_list(self, requests_mock):
        fileAtts = instruments.get(1).get_log_entry(1).get_file_attachment_list()
        assert len(fileAtts) == 3
        
    def test_get_file_attachment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).get_log_entry(1).get_file_attachment('Test')
        
    def test_get_file_attachment_success(self, requests_mock):
        fileAtt = instruments.get(1).get_log_entry(1).get_file_attachment(1)
        assert fileAtt is not None
        
    def test_get_file_attachment_properties(self, requests_mock):
        fileAtt = instruments.get(1).get_log_entry(1).get_file_attachment(1)
        assert fileAtt.file_attachment_id == 1
        assert fileAtt.file_name == 'TestName'
        assert fileAtt.content == 'TestContent'
        assert 'InstrumentLogFileAttachment' in repr(fileAtt)
    
    def test_get_object_attachment_list(self, requests_mock):
        objAtts = instruments.get(1).get_log_entry(1).get_object_attachment_list()
        assert len(objAtts) == 3
        
    def test_get_object_attachment_fail(self, requests_mock):
        with pytest.raises(TypeError):
            instruments.get(1).get_log_entry(1).get_object_attachment('Test')
            
    def test_get_object_attachment_success(self, requests_mock):
        objAtt = instruments.get(1).get_log_entry(1).get_object_attachment(1)
        assert objAtt is not None
        
    def test_get_object_attachment_properties(self, requests_mock):
        objAtt = instruments.get(1).get_log_entry(1).get_object_attachment(1)
        assert objAtt.object_attachment_id == 1
        assert objAtt.object_id == 1
        assert 'InstrumentLogObjectAttachment' in repr(objAtt)