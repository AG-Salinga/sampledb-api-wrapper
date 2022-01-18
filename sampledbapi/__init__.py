import json
from typing import Dict, List

import requests

__all__ = ["authenticate", "actions", "actiontypes", "instruments",
           "locations", "objects", "users"]

_address = None
_api_key = None


class SampleDBObject:

    def __init__(self, d: Dict = None):
        """Initialize class attributes from dictionary."""
        if d is not None:
            for key in dir(self):
                if not key.startswith("__") and key in d:
                    setattr(self, key, d[key])


def authenticate(address: str, api_key: str):
    global _address, _api_key
    old_address, old_key = _address, _api_key
    _address, _api_key = address, api_key
    try:
        getData("actions")
    except requests.exceptions.HTTPError as e:
        _address, _api_key = old_address, old_key
        raise Exception("Authentication not successful: " + str(e))


def __headers() -> Dict:
    return {"Authorization": "Bearer " + _api_key}


def getData(path: str) -> str:
    if _address is not None:
        address = _address + "/api/v1/" + path
        r = requests.get(address, headers=__headers())
        if r.status_code == 200 or r.status_code == 201:
            try:
                return json.loads(r.text)
            except Exception as e:
                # We need better error handling here
                raise Exception("JSON could not be parsed: " + str(e) +
                                "\nJSON was\n" + r.text)
        else:
            r.raise_for_status()
    else:
        raise Exception("You have to authenticate first.")


def postData(path: str, data) -> requests.Response:
    if _address is not None:
        address = _address + "/api/v1/" + path
        data = json.dumps(data)
        requests.post(address, headers=__headers(), data=data).raise_for_status()
    else:
        raise Exception("You have to authenticate first.")


def putData(path: str, data) -> requests.Response:
    if _address is not None:
        address = _address + "/api/v1/" + path
        data = json.dumps(data)
        requests.put(address, headers=__headers(), data=data).raise_for_status()
    else:
        raise Exception("You have to authenticate first.")
