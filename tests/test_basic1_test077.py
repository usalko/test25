from unittest import TestCase

from basic1 import test077


class TestsBasic1Test077(TestCase):
    '''
    Write a Python program to test whether the system is a big-endian platform or a little-endian platform.
    '''

    def test_case1(self):
        self.assertEqual(
            test077(),
            None,
        )
