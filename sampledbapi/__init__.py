import json
from typing import Dict, List

import requests

__all__ = ["authenticate", "actions", "actiontypes", "instruments",
           "locations", "objects", "users"]

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
        raise Exception("JSON could not be parsed: " + str(e) +
                        "\nJSON was\n" + r.text)


def postData(path: str, data) -> requests.Response:
    address = _address + "/api/v1/" + path
    data = json.dumps(data)
    return requests.post(address, headers=__headers(), data=data)


def putData(path: str, data) -> requests.Response:
    address = _address + "/api/v1/" + path
    data = json.dumps(data)
    return requests.put(address, headers=__headers(), data=data)
