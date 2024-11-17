from unittest import TestCase

from basic1 import test054


class TestsBasic1Test054(TestCase):
    '''
    Write a Python program to get the current username.
    '''

    def test_case1(self):
        self.assertEqual(
            test054(),
            None,
        )
