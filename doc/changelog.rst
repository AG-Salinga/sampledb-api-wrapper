Changelog
=========

Version 0.6.5
-------------

- Return server response text on 4xx errors (thanks to Malte Deckers)
- Include missing submodules in documentation (thanks to Malte Deckers)
- Tests also run on Python 3.12
- Add url and hash to File object (thanks to Malte Deckers)
- Add new object log entries endpoint (thanks to Malte Deckers)
- Fix some type annotations and checks

Version 0.6.4
-------------

- No changes

Version 0.6.3
-------------

- Added return of id if objects are created

Version 0.6.2
-------------

- Added new endpoint "Getting related objects"
- Increased test coverage

Version 0.6.1
-------------

- Update examples in Readme

Version 0.6.0
-------------

- Breaking change: All methods are now snake case (instead of camel case)
- Test user authentication based on "/users/me"
- Repository is now mirrored to Github

Version 0.5.0
-------------

- Implementation of location types
- object.getLocation now returns a LocationOccurrence rather than a Location
- Added unit tests, static type checks and coverage report
- Several important bug fixes

Version 0.4.0
-------------

- Breaking change in the API of objects and instruments: Most methods are now direclty assigned to the respective objects
- Some more examples in documentation

Version 0.3.4
-------------

- Add more exeamples to the documentation

Version 0.3.3
-------------

- Display Readme on PyPi and in documentation

Version 0.3.2
-------------

- Use Gitlab Pages for documentation

Version 0.3.1
-------------

- Added Matlab example
- "authenticate" now checks immediately if the credentials were correct

Version 0.3.0
-------------

- Added a class structure that makes working with the data easier

Version 0.2.1
-------------

- Fixed some string formatting issues

Version 0.2.0
-------------

- Better documentation

Version 0.1.0
-------------

- Reached feature parity with the HTTP API
