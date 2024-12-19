from unittest import TestCase

from basic1 import test143


class TestsBasic1Test143(TestCase):
    '''
    Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.
    '''

    def test_case1(self):
        self.assertEqual(
            test143(),
            None,
        )
