from unittest import TestCase

from basic1 import test142


class TestsBasic1Test142(TestCase):
    '''
    Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
    Original sequence: 01010101
    Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
    True
    Original sequence: 00
    Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
    False
    Original sequence: 000111000111
    Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
    True
    Original sequence: 00011100011
    Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
    False
    '''

    def test_case1(self):
        self.assertEqual(
            test142(),
            None,
        )
