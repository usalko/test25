from unittest import TestCase

from basic1 import test042


class TestsBasic1Test042(TestCase):
    '''
    Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
    '''

    def test_case1(self):
        self.assertEqual(
            test042(),
            None,
        )

