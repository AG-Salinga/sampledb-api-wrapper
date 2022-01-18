# SampleDB API Wrapper
## What it does
This package is a simple Python wrapper for the [HTTP API](https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html) of [SampleDB](https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/), a web-based sample and measurement metadata database developed at PGI and JCNS.

This Python wrapper may also be used e.g. in Matlab and Julia.

## Installation
User installation using pip:
```
pip install --upgrade --user sampledbapi
```

System installation using pip:
```
pip install --upgrade sampledbapi
```

## Example usage

### Python
```python
from sampledbapi import *

server_address = ...
api_key = ...

# Authentication
authenticate(server_address, api_key)

# Simple queries
print(actions.getList())
print(objects.get(123))
print(instruments.getList())

# Advanced search
print(objects.getList("material == \"Sb\""))
```

### Matlab

You need a working installation of Python and `sampledbapi` installed for this to work.
Some type conversions are needed (e.g. to pass integers).

```matlab
% Authentication
py.sampledbapi.authenticate("https://...", "your_api_key")

% Simple queries
print(instruments.getList())
py.sampledbapi.objects.get(py.int(123))
py.sampledbapi.instruments.getList())

% Advanced search
l = py.sampledbapi.objects.getList('material == "Sb"')
obj = l{1}
obj.data
```

## Documentation

The current API documentation can be found [here](https://zivgitlab.uni-muenster.de/ag-salinga/sampledb-api-wrapper/-/jobs/artifacts/v0.3.0/file/doc/_build/index.html?job=deploy_production).
Further details on the input and output of each function (usually JSON) can be found in the documentation of the [HTTP API](https://scientific-it-systems.iffgit.fz-juelich.de/SampleDB/developer_guide/api.html).

## What works

The full HTTP API of SampleDB is supported. This includes

- [x] Authentication
- [x] Objects
    - [x] Reading a list of all objects
    - [x] Getting the current object version
    - [x] Reading an object version
    - [x] Creating a new object
    - [x] Updating an object / Creating a new object version
- [x] Object permissions
    - [x] Reading whether an object is public
    - [x] Setting whether an object is public
    - [x] Reading all users' permissions
    - [x] Reading a user's permissions
    - [x] Setting a user's permissions
    - [x] Reading all groups' permissions
    - [x] Reading a group's permissions
    - [x] Setting a group's permissions
    - [x] Reading all project groups' permissions
    - [x] Reading a project group's permissions
    - [x] Setting a project group's permissions
- [x] Instruments
    - [x] Reading a list of all instruments
    - [x] Reading an instrument
- [x] Instrument log entries
    - [x] Reading a list of all log entries for an instrument
    - [x] Reading an instrument log entry
    - [x] Reading a list of all log categories for an instrument
    - [x] Reading an instrument log category
    - [x] Reading a list of all file attachments for a log entry
    - [x] Reading a file attachment for a log entry
    - [x] Reading a list of all object attachments for a log entry
    - [x] Reading an object attachment for a log entry
    - [x] Creating an instrument log entry
- [x] Actions
    - [x] Reading a list of all actions
    - [x] Reading an action
- [x] Action types
    - [x] Reading a list of all action types
    - [x] Reading an action type
- [x] Users
    - [x] Reading a list of all users
    - [x] Reading a user
    - [x] Reading the current user
- [x] Locations
    - [x] Reading a list of all locations
    - [x] Reading a location
    - [x] Reading a list of an object's locations
    - [x] Reading an object's location
- [x] Files
    - [x] Reading a list of an object's files
    - [x] Reading information for a file
    - [x] Uploading a file
    - [x] Posting a link
- [x] Comments
    - [x] Reading a list of an object’s comments
    - [x] Reading information for a comment
    - [x] Posting a comment
