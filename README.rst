===========
HTTP Status
===========

A simple HTTP status code/name/description library for Python.

------------
Installation
------------

Either install via pip::

    $ pip install http-status

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

"THE BEER-WARE LICENSE" (Revision 42):
<danneh@danneh.net> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
