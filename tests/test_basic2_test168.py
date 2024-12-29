from unittest import TestCase

from basic2 import test168


class TestsBasic1Test168(TestCase):
    '''18. Find Median of Three

Write a Python program to find the median among three given numbers.
'''

    def test_case1(self):
        self.assertListEqual(
            test168(2),
            [11, 69, 88, 96],
        )
