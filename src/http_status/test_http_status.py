# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <Chad Nelson> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me hot coco in return Chad Nelson.
# ----------------------------------------------------------------------------
__author__ = 'Chad Nelson'
from unittest import TestCase, main
from http_status import Status, NoneStatus
from formencode import Invalid


class HTTPStatusTestCase(TestCase):
    correct_code = 404
    correct_name = u'Not Found'
    correct_description = u'Server cannot find requested resource.'
    correct_unicode_verbose = u'HTTP {} {} {}'.format(correct_code, correct_name, correct_description)
    correct_unicode = u'HTTP {} {}'.format(correct_code, correct_name)
    undefined_code = 480    # Undefined but still in valid range.
    default_code = 200
    default_name_fail = u'No HTTP Name'
    default_description_fail = u'No HTTP Description'
    alt_name_fail = u'some name'
    alt_description_fail = u'some description'
    below_min_code = 0
    exceeds_max_code = 777
    non_numeric_code = u'82ab32z!'


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
        with self.assertRaises(Invalid):
            Status(code=self.exceeds_max_code)

    def test_below_min_code(self):
        with self.assertRaises(Invalid):
            Status(code=self.below_min_code)

    def test_non_numeric_code(self):
        with self.assertRaises(Invalid):
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
