from unittest import TestCase

from basic1 import test140


class TestsBasic1Test140(TestCase):
    '''
    Write a Python program to convert an integer to binary that keeps leading zeros.
    Sample data : x=12
    Expected output : 00001100
    0000001100
    '''

    def test_case1(self):
        self.assertEqual(
            test140(),
            None,
        )
