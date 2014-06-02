===========
HTTP Status
===========

A simple HTTP status code/name/description library for Python.

------------
Installation
------------

Either install via pip::

    $ pip install http_status

Or clone the git repo, and run setup.py::

    $ git clone https://github.com/DanielOaks/http_status.git
    Cloning into 'http_status'...
    [...]
    Unpacking objects: 100% (18/18), done.

    $ cd http_status/

    $ python setup.py build install
    running build
    [...]
    Writing /usr/local/lib/python2.7/site-packages/http_status-0.1.0a-py2.7.egg-info

-----
Usage
-----

Use by itself::

    >>> import http_status
    >>> http_status.name[302]
    'Found'
    >>> http_status.description[302]
    'URI of this resource has changed, temporarily.'

Use of the Status object::

    >>> from http_status import Status
    >>> s = Status(403)
    >>> s.code
    403
    >>> s.name
    'Forbidden'
    >>> s.description
    'Client does not have rights to access the content.'

    >>> s.code = 405
    >>> s.name
    'Method Not Allowed'
    >>> s.description
    'Server has disabled this request method and cannot be used.'

Note that if the Status object does not have a name/description matching the
given code, it will return default strings (for compatability when directly
inserting ``Status.name`` and ``Status.description`` into format strings.

This can be changed by passing arguments ``name_fail`` and
``description_fail`` when you create Status::

    >>> from http_status import Status
    >>> s = Status(2435)
    >>> s.name
    'No HTTP Name'
    >>> s.description
    'No HTTP Description.'

    >>> from http_status import Status
    >>> s = Status(2435, name_fail='Nothing', description_fail='Nothing at all')
    >>> s.name
    'Nothing'
    >>> s.description
    'Nothing at all'

The class ``NoneStatus`` is exactly the same as Status, but ``name_fail``
and ``description_fail`` both default to None.

-------
Sources
-------

Descriptions mostly adapted from:

- Mozilla Dev Wiki: <https://developer.mozilla.org/en-US/docs/HTTP/HTTP_response_codes>
- Wikipedia: <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>

-------
License
-------

Copyright (c) 2014 Daniel Oaks and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
