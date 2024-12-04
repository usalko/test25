from unittest import TestCase

from basic1 import test105


class TestsBasic1Test105(TestCase):
    '''
    Write a Python program to get the users environment.
    '''

    def test_case1(self):
        self.assertEqual(
            test105(),
            None,
        )
