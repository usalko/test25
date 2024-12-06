from unittest import TestCase

from basic1 import test110


class TestsBasic1Test110(TestCase):
    '''
    Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
    '''

    def test_case1(self):
        self.assertEqual(
            test110(),
            None,
        )
