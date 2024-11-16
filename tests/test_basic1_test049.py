from unittest import TestCase

from basic1 import test049


class TestsBasic1Test049(TestCase):
    '''
    Write a Python program to list all files in a directory.
    '''

    def test_case1(self):
        self.assertEqual(
            test049(),
            None,
        )

