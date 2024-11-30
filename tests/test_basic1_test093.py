from unittest import TestCase

from basic1 import test093


class TestsBasic1Test093(TestCase):
    '''
    Write a Python program to get the Identity, Type, and Value of an object.
    '''

    def test_case1(self):
        self.assertEqual(
            test093(),
            None,
        )
