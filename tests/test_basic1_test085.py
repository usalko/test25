from unittest import TestCase

from basic1 import test085


class TestsBasic1Test085(TestCase):
    '''
    Write a Python program to check whether a file path is a file or a directory.
    '''

    def test_case1(self):
        self.assertEqual(
            test085(),
            None,
        )
