from unittest import TestCase

from basic1 import test066


class TestsBasic1Test066(TestCase):
    '''
    Write a Python program to calculate the body mass index.
    '''

    def test_case1(self):
        self.assertEqual(
            test066(),
            None,
        )
