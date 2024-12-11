from unittest import TestCase

from basic1 import test124


class TestsBasic1Test124(TestCase):
    '''
    Write a Python program to check whether multiple variables have the same value.
    '''

    def test_case1(self):
        self.assertEqual(
            test124(),
            None,
        )
