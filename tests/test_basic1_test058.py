from unittest import TestCase

from basic1 import test058


class TestsBasic1Test058(TestCase):
    '''
    Write a Python program to sum the first n positive integers.
    '''

    def test_case1(self):
        self.assertEqual(
            test058(3),
            6,
        )
