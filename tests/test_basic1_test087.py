from unittest import TestCase

from basic1 import test087


class TestsBasic1Test087(TestCase):
    '''
    Write a Python program to get the size of a file.
    '''

    def test_case1(self):
        self.assertEqual(
            test087(),
            None,
        )
