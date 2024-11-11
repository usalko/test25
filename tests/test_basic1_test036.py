from unittest import TestCase

from basic1 import test036


class TestsBasic1Test036(TestCase):
    '''
    Write a Python program to add two objects if both objects are integers.
    '''

    def test_case1(self):
        self.assertEqual(
            test036(1, {}),
            None,
        )

    def test_case1(self):
        self.assertEqual(
            test036(1, 2),
            3,
        )
