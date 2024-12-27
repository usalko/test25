from unittest import TestCase

from basic2 import test167


class TestsBasic1Test167(TestCase):
    '''17. Strobogrammatic Numbers

Write a Python program to get all strobogrammatic numbers that are of length n.
A strobogrammatic number is a number whose numeral is rotationally symmetric,
so that it appears the same when rotated 180 degrees.
In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
For example,
Given n = 2, return ["11", "69", "88", "96"].
Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']
'''

    def test_case1(self):
        self.assertListEqual(
            test167(2),
            [11, 69, 88, 96],
        )

    def test_case2(self):
        self.assertListEqual(
            test167(3),
            [111, 818, 916, 619, 808, 191, 906, 609, 888, 181, 986, 689],
        )
