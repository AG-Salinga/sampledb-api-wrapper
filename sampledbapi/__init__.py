import json
from typing import Any, Dict

import requests

__all__ = ["authenticate", "actions", "actiontypes", "instruments",
           "locations", "locationtypes", "objects", "users"]

_address = None
_api_key = None


class SampleDBObject:

    def __init__(self, d: Dict):
        """Initialize class attributes from dictionary."""
        for key in dir(self):
            if not key.startswith("__") and key in d:
                setattr(self, key, d[key])


def authenticate(address: str, api_key: str):
    """Authenticate with a SampleDB instance

    To retrieve data from SampleDB and upload data to it, you have to
    authenticate first.

    Arguments:
        address: URL of the SampleDB server.
        api_key: API token you can generate using "Preferences/API Tokens".
    """

    global _address, _api_key
    old_address, old_key = _address, _api_key
    _address, _api_key = address, api_key
    try:
        get_data("users/me")
    except requests.exceptions.HTTPError as e:
        _address, _api_key = old_address, old_key
        raise Exception("Authentication not successful: " + str(e))


def __headers() -> Dict:
    if _api_key is not None:
        return {"Authorization": "Bearer " + _api_key}
    else:
        raise Exception("You need to provide an API key.")


def get_data(path: str) -> Any:
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


def post_data(path: str, data):
    if _address is not None:
        address = _address + "/api/v1/" + path
        data = json.dumps(data)
        requests.post(address, headers=__headers(),
                      data=data).raise_for_status()
    else:
        raise Exception("You have to authenticate first.")


def put_data(path: str, data):
    if _address is not None:
        address = _address + "/api/v1/" + path
        data = json.dumps(data)
        requests.put(address, headers=__headers(),
                     data=data).raise_for_status()
    else:
        raise Exception("You have to authenticate first.")
