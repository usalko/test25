from unittest import TestCase

from basic2 import test183


class TestsBasic1Test183(TestCase):
    '''33. Sum Digit Count
 
Write a Python program to compute the digit number of the sum of two given integers.
Input:
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 <= x, y <= 1,000,000
Input two integers(a b):
5 7
Sum of two integers a and b.:
2
    '''

    def test_case1(self):
        self.assertListEqual(
            test183(2),
            0,
        )
