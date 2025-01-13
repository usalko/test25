from unittest import TestCase

from basic2 import test176


class TestsBasic1Test176(TestCase):
    '''26. Absolute Pairwise Difference

Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).
Sample array: [1, 2, 3]
Then all the distinct pairs will be:
1 2
1 3
2 3
    '''

    def test_case1(self):
        self.assertListEqual(
            test176(2),
            0,
        )
