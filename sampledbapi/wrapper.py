from typing import List
import requests

class SampleDB:

    def __init__(self, address: str, api_key: str):
        self.__address = address
        self.__api_key = api_key

    @property
    def address(self) -> str:
        return self.__address

    @property
    def api_key(self) -> str:
        return self.__api_key

    def getObjectList(self) -> List:
        return []
