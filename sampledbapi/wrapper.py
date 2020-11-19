import json
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

    @property
    def __headers(self) -> dict:
        return {"Authorization": "Bearer " + self.api_key}

    def __get(self, path: str) -> str:
        address = self.address + "/api/v1/" + path
        r = requests.get(address, headers=self.__headers)
        return r.text

    def getObjectList(self) -> List:
        return json.loads(self.__get("objects"))

    def getCurrentObjectVersion(self, object_id: int):
        if isinstance(object_id, int):
            return json.loads(self.__get("objects/{}".format(object_id)))
        else:
            raise TypeError()
