from unittest import TestCase

from basic1 import test125


class TestsBasic1Test125(TestCase):
    '''
    Write a Python program to sum all counts in a collection.
    '''

    def test_case1(self):
        self.assertEqual(
            test125(),
            None,
        )
