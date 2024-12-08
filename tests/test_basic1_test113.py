from unittest import TestCase

from basic1 import test113, NotANumberException


class TestsBasic1Test113(TestCase):
    '''
    Write a Python program that inputs a number and generates an error message if it is not a number.
    '''

    def test_case1(self):
        self.assertEqual(
            test113(1),
            True,
        )

    def test_case2(self):
        self.assertRaises(
            NotANumberException,
            test113,
            ''
        )