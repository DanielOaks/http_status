#!/usr/bin/env python
# written by Daniel Oaks <daniel@danieloaks.net>, Chad Nelson
# licensed under the BSD 2-clause license

__author__ = 'Chad Nelson'

import six
from unittest import TestCase, main
from http_status import Status, NoneStatus, InvalidHttpCode


class HTTPStatusTestCase(TestCase):
    correct_code = 404
    correct_name = 'Not Found'
    correct_description = 'Server cannot find requested resource.'
    correct_unicode_verbose = six.u('HTTP {} {}: {}').format(correct_code, correct_name, correct_description)
    correct_unicode = six.u('HTTP {} {}').format(correct_code, correct_name)
    undefined_code = 480  # Undefined but still in valid range.
    default_code = 200
    default_name_fail = 'No HTTP Name'
    default_description_fail = 'No HTTP Description'
    alt_name_fail = 'some name'
    alt_description_fail = 'some description'
    below_min_code = 0
    exceeds_max_code = 777
    non_numeric_code = '82ab32z!'


class StatusTest(HTTPStatusTestCase):
    def test_default_code(self):
        HTTP_Status = Status()
        self.assertEqual(HTTP_Status.code, self.default_code)

    def test_correct_code(self):
        HTTP_Status = Status(code=self.correct_code)
        self.assertEqual(HTTP_Status.name, self.correct_name)
        self.assertEqual(HTTP_Status.description, self.correct_description)

    def test_undefined_code(self):
        HTTP_Status = Status(code=self.undefined_code)
        self.assertEqual(HTTP_Status.name, self.default_name_fail)
        self.assertEqual(HTTP_Status.name, HTTP_Status.name_fail)
        self.assertEqual(HTTP_Status.description, self.default_description_fail)
        self.assertEqual(HTTP_Status.description, HTTP_Status.description_fail)

    def test_alt_name_description(self):
        HTTP_Status = Status(
            code=self.undefined_code,
            name_fail=self.alt_name_fail,
            description_fail=self.alt_description_fail
        )
        self.assertEqual(HTTP_Status.name, self.alt_name_fail)
        self.assertEqual(HTTP_Status.name, HTTP_Status.name_fail)
        self.assertEqual(HTTP_Status.description, self.alt_description_fail)
        self.assertEqual(HTTP_Status.description, HTTP_Status.description_fail)

    def test_exceeds_max_code(self):
        with self.assertRaises(InvalidHttpCode):
            Status(code=self.exceeds_max_code)

    def test_below_min_code(self):
        with self.assertRaises(InvalidHttpCode):
            Status(code=self.below_min_code)

    def test_non_numeric_code(self):
        with self.assertRaises(InvalidHttpCode):
            Status(code=self.non_numeric_code)

    def test__unicode__(self):
        HTTP_Status = Status(code=self.correct_code)
        self.assertEqual(HTTP_Status.__unicode__(verbose=True), self.correct_unicode_verbose)
        self.assertEqual(HTTP_Status.__unicode__(verbose=False), self.correct_unicode)


class NoneStatusTest(HTTPStatusTestCase):
    def test_code_match(self):
        HTTP_NoneStatus = NoneStatus(code=self.correct_code)
        HTTP_Status = Status(code=self.correct_code)
        self.assertEqual(HTTP_NoneStatus.code, HTTP_Status.code)


if __name__ == '__main__':
    main()
