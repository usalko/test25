from unittest import TestCase

from basic1 import test137


class TestsBasic1Test137(TestCase):
    '''
    Write a Python program to find files and skip directories in a given directory.
    '''

    def test_case1(self):
        self.assertEqual(
            test137(),
            None,
        )
