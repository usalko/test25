from unittest import TestCase

from basic1 import test053
from os import environ


class TestsBasic1Test053(TestCase):
    '''
    Write a Python program to access environment variables.
    '''

    def test_case1(self):
        TEST_VARIABLE = 'Test053'
        environ['TEST_VARIABLE'] = TEST_VARIABLE
        self.assertEqual(
            test053('TEST_VARIABLE'),
            TEST_VARIABLE,
        )
