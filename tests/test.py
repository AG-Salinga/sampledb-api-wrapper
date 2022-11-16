from unittest import *
from unittest.mock import Mock, patch
#from sampledbapi import locations, authenticate

class LoginTestCase(TestCase):
    def test1(self):
        self.assertRaises(Exception, None)
        
class LocationsTestCase():
    
    def __init__(self, *args, **kwargs):
        super(LocationsTestCase, self).__init__(*args, **kwargs)
        #server_address = "http://128.176.208.107:8000"
        #api_key = "738b5d4bb896fdc318f5f3beeea01a5c2c72686af3563c2db2163995229e8029"
        #server_address = "https://sampledb.ag-salinga.wwu.de"
        #api_key = "c1e55fb447cc50e9489022fd705b0a389820a6a93476d1b12f20579f6bd52742"
        #authenticate(server_address, api_key)
    
    def test1(self):
        self.assertTrue(True)
        #server_address = "http://128.176.208.107:8000"
        #api_key = "738b5d4bb896fdc318f5f3beeea01a5c2c72686af3563c2db2163995229e8029"
        #server_address = "https://sampledb.ag-salinga.wwu.de"
        #api_key = "c1e55fb447cc50e9489022fd705b0a389820a6a93476d1b12f20579f6bd52742"
        #authenticate(server_address, api_key)
        
        #locs = locations.getList()
        #self.assert()