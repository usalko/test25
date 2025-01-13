from unittest import TestCase

from basic2 import test182


class TestsBasic1Test182(TestCase):
    '''32. Top Three Building Heights

Write a Python program to find the heights of the top three buildings in descending order from eight given buildings.
Input:
0 <= height of building (integer) <= 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Heights of the top three buildings:
45
39
37
    '''

    def test_case1(self):
        self.assertListEqual(
            test182(2),
            0,
        )
