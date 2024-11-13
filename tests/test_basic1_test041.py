from unittest import TestCase

from basic1 import test041


class TestsBasic1Test041(TestCase):
    '''
    Write a Python program to check whether a file exists.
    '''

    def test_case1(self):
        self.assertEqual(
            test041(),
            None,
        )

