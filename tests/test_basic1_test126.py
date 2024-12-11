from unittest import TestCase

from basic1 import test126


class TestsBasic1Test126(TestCase):
    '''
    Write a Python program to get the actual module object for a given object.
    '''

    def test_case1(self):
        self.assertEqual(
            test126(),
            None,
        )
