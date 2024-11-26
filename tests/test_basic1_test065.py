from unittest import TestCase

from basic1 import test065


class TestsBasic1Test065(TestCase):
    '''
    Write a Python program that converts seconds into days, hours, minutes, and seconds.
    '''

    def test_case1(self):
        self.assertTupleEqual(
            test065(6),
            (0, 0, 0, 6),
        )

    def test_case2(self):
        self.assertTupleEqual(
            test065(66),
            (0, 0, 1, 6),
        )

    def test_case3(self):
        self.assertTupleEqual(
            test065(666),
            (0, 0, 11, 6),
        )

    def test_case4(self):
        self.assertTupleEqual(
            test065(6666),
            (0, 1, 51, 6),
        )

    def test_case5(self):
        self.assertTupleEqual(
            test065(66666),
            (0, 18, 31, 6),
        )

    def test_case6(self):
        self.assertTupleEqual(
            test065(666666),
            (7, 17, 11, 6),
        )
