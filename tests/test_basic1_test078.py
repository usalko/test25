from unittest import TestCase

from basic1 import test078


class TestsBasic1Test078(TestCase):
    '''
    Write a Python program to find the available built-in modules.
    '''

    def test_case1(self):
        self.assertEqual(
            test078(),
            None,
        )
