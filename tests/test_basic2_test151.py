from unittest import TestCase

from basic2 import test151


class TestsBasic1Test151(TestCase):
    '''1. Unique Numbers Check

    Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
    '''

    def test_case1(self):
        self.assertEqual(
            test151(),
            None,
        )
