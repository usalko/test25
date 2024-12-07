from unittest import TestCase

from basic1 import test103


class TestsBasic1Test103(TestCase):
    '''
    Write a Python program to extract the filename from a given path.
    '''

    def test_case1(self):
        self.assertEqual(
            test103('./any/any/path.txt'),
            'path.txt',
        )
