from unittest import TestCase

from basic1 import test121


class TestsBasic1Test121(TestCase):
    '''
    Write a Python program to determine if a variable is defined or not.
    '''

    def test_case1(self):
        self.assertEqual(
            test121(),
            None,
        )
