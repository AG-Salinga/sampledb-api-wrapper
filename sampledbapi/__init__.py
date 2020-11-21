import json
import requests
from typing import Dict, List

__all__ = ["authenticate", "actions", "actiontypes", "files",
           "instruments", "locations", "objects", "permissions", "users"]

_address = None
_api_key = None


def authenticate(address: str, api_key: str):
    global _address, _api_key
    _address = address
    _api_key = api_key


def __headers() -> Dict:
    return {"Authorization": "Bearer " + _api_key}


def getData(path: str) -> str:
    address = _address + "/api/v1/" + path
    r = requests.get(address, headers=__headers())
    try:
        return json.loads(r.text)
    except Exception as e:
        # We need better error handling here
        raise Exception("JSON could not be parsed.")
