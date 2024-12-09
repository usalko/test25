from unittest import TestCase

from basic1 import test118


class TestsBasic1Test118(TestCase):
    '''
    Write a Python program to create a bytearray from a list.
    '''

    def test_case1(self):
        self.assertEqual(
            test118(),
            None,
        )
