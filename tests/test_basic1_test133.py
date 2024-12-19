from unittest import TestCase

from basic1 import test133


class TestsBasic1Test133(TestCase):
    '''
    Write a Python program to calculate the time runs (difference between start and current time) of a program.
    '''

    def test_case1(self):
        self.assertEqual(
            test133(),
            None,
        )
