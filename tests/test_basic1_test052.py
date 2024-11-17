from unittest import TestCase

from basic1 import test052


class TestsBasic1Test052(TestCase):
    '''
    Write a Python program to print to STDERR.
    '''

    def test_case1(self):
        self.assertEqual(
            test052(),
            None,
        )
