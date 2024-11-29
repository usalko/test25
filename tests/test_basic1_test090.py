from unittest import TestCase

from basic1 import test090


class TestsBasic1Test090(TestCase):
    '''
    Write a Python program to create a copy of its own source code.
    '''

    def test_case1(self):
        self.assertEqual(
            test090(),
            None,
        )
