from unittest import TestCase

from basic2 import test171


class TestsBasic1Test171(TestCase):
    '''21. Notes Count from Amount

Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) against an amount.
Range - Number of notes(n) : n (1 <= n <= 1000000).
'''

    def test_case1(self):
        self.assertListEqual(
            test171(2),
            0,
        )
