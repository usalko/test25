from unittest import TestCase

from basic2 import test154


class TestsBasic1Test154(TestCase):
    '''4. Zero Sum Triplets

    Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers.
    '''

    def test_case1(self):
        self.assertEqual(
            test154(),
            None,
        )
