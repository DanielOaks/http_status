#!/usr/bin/env python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <danneh@danneh.net> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Daniel Oakley
# ----------------------------------------------------------------------------

"""HTTP status codes, names, and descriptions.

:mod:`http_status` provides names and descriptions for HTTP status codes, as
well as a Status object to abstract all that out, for general use.

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
and ``description_fail`` both default to None."""

# Source 1: Hypertext Transfer Protocol -- HTTP/1.1 RFC 2616 Fielding, et al.
#           http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
# Source 2: http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# Source of the status code and description is assumed to be Source 1 unless otherwise noted.

# Names of HTTP status codes.
name = {
    # Informational.
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',

    # Success
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi-Status',        # WebDAV; RFC 4918
    208: "Already Reported",    # WebDAV; RFC 5842
    226: "IM Used",             # RFC 3229

    # Redirection
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: 'Switch Proxy',        # HTTP/1.1 No longer used
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',  # Approved as experimental RFC http://en.wikipedia.org/wiki/Request_for_Comments

    # Client Error.
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request-URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    418: 'I\'m a Teapot',               # RFC 2324 April Fool's Joke
    419: 'Authentication Timeout',      # RFC 2616 not part of HTTP standard
    422: 'Unprocessable Entity',        # WebDAV; RFC 4918
    423: 'Locked',                      # WebDAV; RFC 4918
    424: 'Failed Dependency',           # WebDAV; RFC 4918
    425: 'Unordered Collection',        # Defined in drafts of "WebDAV Advanced Collections Protocol"
    426: 'Upgrade Required',            # RFC 2817
    428: 'Precondition Required',       # RFC 6585 http://tools.ietf.org/html/rfc6585
    429: 'Too Many Requests',           # RFC 6585 http://tools.ietf.org/html/rfc6585
    431: 'Header Fields Too Large',     # RFC 6585 http://tools.ietf.org/html/rfc6585
    440: 'Login Timeout',               # Microsoft
    444: 'No Response',                 # Nginx
    449: 'Retry With',                  # Microsoft
    450: 'Blocked By Windows Parental Controls',    # Microsoft
    451: 'Unavailable For Legal Reasons',           # Internet Draft http://en.wikipedia.org/wiki/HTTP_451
    494: 'Request Header Too Large',    # Nginx
    495: 'Cert Error',                  # Nginx
    496: 'No Cert',                     # Nginx
    497: 'HTTP to HTTPS',               # Nginx
    499: 'Client Closed Request',       # Nginx

    # Server Error.
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',     # RFC 2295
    507: 'Insufficient Storage',        # WebDAV; RFC 4918
    508: 'Loop Detected',               # WebDAV; RFC 5842
    509: 'Bandwidth Limit Exceeded',    # Apache bw/limited extension
    510: 'Not Extended',                # RFC 2774
    511: 'Network Authentication'       # RFC 6585
}

# Descriptions of HTTP status codes.
description = {
    # Informational.
    100: 'Continue with the request.',
    101: 'Server is switching to a different protocol.',
    102: 'Server has received and is processing the request, but no response is available yet.',

    # Success
    200: 'Request was successful.',
    201: 'Request was successful, and a new resource has been created.',
    202: 'Request has been accepted but not yet acted upon.',
    203: 'Request was successful, but server is returning information that may be from another source.',
    204: 'There is no content to send for this request, but the headers may be useful.',
    205: 'Server successfully processed the request, but is not returning any content.',
    206: 'Download is separated into multiple streams, due to range header.',
    207: 'Message body that follows is an XML message and can contain a number of separate response codes.',
    208: ('Response is a representation of the result of one or more instance-manipulations applied to the current ' +
          'instance.'),
    226: ('The server has fulfilled a GET request for the resource, and the response is a representation of the ' +
          'result of one or more instance-manipulations applied to the current instance.'),

    # Redirection.
    300: 'Request has more than one possible response.',
    301: 'URI of this resource has changed.',
    302: 'URI of this resource has changed, temporarily.',
    303: 'Client should get this resource from another URI.',
    304: 'Response has not been modified, client can continue to use a cached version.',
    305: 'Requested resource may only be accessed through a given proxy.',
    306: 'No longer used. Requested resource may only be accessed through a given proxy.',
    307: 'URI of this resource has changed, temporarily. Use the same HTTP method to access it.',
    308: 'The request, and all future requests should be repeated using another URI.',

    # Client Error.
    400: 'Server could not understand the request, due to invalid syntax.',
    401: 'Authentication is needed to access the given resource.',
    402: 'Some form of payment is needed to access the given resource.',
    403: 'Client does not have rights to access the content.',
    404: 'Server cannot find requested resource.',
    405: 'Server has disabled this request method and cannot be used.',
    406: 'Requested resource is only capable of generating content not acceptable according to the Accept headers sent.',
    407: 'Authentication by a proxy is needed to access the given resource.',
    408: 'Server would like to shut down this unused connection.',
    409: 'Request could not be processed because of conflict in the request, such as an edit conflict.',
    410: 'Requested content has been delected from the server',
    411: 'Server requires the Content-Length header to be defined.',
    412: 'Client has indicated preconditions in its headers which the server does not meet.',
    413: 'Request entity is larger than limits defined by server.',
    414: 'URI requested by the client is too long for the server to handle.',
    415: 'Media format of the requested data is not supported by the server.',
    416: "Range specified by the Range header in the request can't be fulfilled.",
    417: "Expectation indicated by the Expect header can't be met by the server.",
    418: 'HTCPCP server is a teapot; the resulting entity body may be short and stout.',
    422: 'Request was well-formed but was unable to be followed due to semantic errors.',
    423: 'Resource that is being accessed is locked.',
    424: 'Request failed due to failure of a previous request (e.g. a PROPPATCH).',
    #425: ('unordered_collection', 'unordered'),
    426: 'Client should switch to a different protocol such as TLS/1.0.',
    428: 'Origin server requires the request to be conditional.',
    429: 'User has sent too many requests in a given amount of time.',
    431: 'Server rejected the request because either a header, or all the headers collectively, are too large.',
    440: 'Your session has expired. (Microsoft)',
    444: 'Server has returned no information to the client and closed the connection (Ngnix).',
    449: 'Request should be retried after performing the appropriate action (Microsoft).',
    450: 'Windows Parental Controls are turned on and are blocking access to the given webpage.',
    451: ('You attempted to access a Legally-restricted Resource. This could be due to censorship or ' +
          'government-mandated blocked access.'),
    494: 'Nginx internal code',
    495: 'SSL client certificate error occurred. (Nginx)',
    496: 'Client did not provide certificate (Nginx)',
    497: 'Plain HTTP request sent to HTTPS port. (Nginx)',
    499: 'Connection has been closed by client while the server is still processing its request (Nginx).',

    # Server Error.
    500: "Server has encountered a situation it doesn't know how to handle.",
    501: 'Request method is not supported by the server and cannot be handled.',
    502: 'Server, while working as a gateway to get a response needed to handle the request, got an invalid response.',
    503: 'Server is not yet ready to handle the request.',
    504: 'Server is acting as a gateway and cannot get a response in time.',
    505: 'HTTP version used in the request is not supported by the server.',
    506: 'Transparent content negotiation for the request results in a circular reference.',
    507: 'Server is unable to store the representation needed to complete the request.',
    508: 'The server detected an infinite loop while processing the request',
    #509: 'This status code, while used by many servers, is not specified in any RFCs.',
    510: 'Further extensions to the request are required for the server to fulfill it.',
    511: 'The client needs to authenticate to gain network access.'
}



class Status(object):
    """Holds an HTTP status code, and provides an easy way to access its name and description."""

    def __init__(self, code=0,
                 name_fail='No HTTP Name',
                 description_fail='No HTTP Description.'):
        self.code = code
        self.name_fail = name_fail
        self.description_fail = description_fail

    @property
    def name(self):
        """Return the name of the current status code as a string."""
        if self.code in name:
            return name[self.code]
        return self.name_fail

    @property
    def description(self):
        """Return the description of the current status code as a string."""
        if self.code in description:
            return description[self.code]
        return self.description_fail


class NoneStatus(Status):
    """Holds an HTTP status code, and provides an easy way to access its name and description."""

    def __init__(self, code=0, name_fail=None, description_fail=None):
        Status.__init__(self, code, name_fail, description_fail)
