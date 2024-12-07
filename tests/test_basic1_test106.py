from unittest import TestCase

from basic1 import test106


class TestsBasic1Test106(TestCase):
    '''
    Write a Python program to divide a path by the extension separator.
    '''

    def test_case1(self):
        self.assertListEqual(
            test106('./path/file.ext'),
            ['./path/file', 'ext'],
        )
