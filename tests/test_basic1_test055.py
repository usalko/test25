from unittest import TestCase

from basic1 import test055


class TestsBasic1Test055(TestCase):
    '''
    Write a Python program to find local IP addresses using Python's stdlib.
    '''

    def test_case1(self):
        self.assertEqual(
            test055(),
            None,
        )
