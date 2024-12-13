from unittest import TestCase

from basic1 import test132


class TestsBasic1Test132(TestCase):
    '''
    Write a Python program to list the home directory without an absolute path.
    '''

    def test_case1(self):
        self.assertEqual(
            test132(),
            None,
        )
