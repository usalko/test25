from unittest import TestCase

from basic1 import test079


class TestsBasic1Test079(TestCase):
    '''
    Write a Python program to get the size of an object in bytes.
    '''

    def test_case1(self):
        self.assertEqual(
            test079(),
            None,
        )
