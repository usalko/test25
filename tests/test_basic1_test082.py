from unittest import TestCase

from basic1 import test082


class TestsBasic1Test082(TestCase):
    '''
    Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
    '''

    def test_case1(self):
        self.assertEqual(
            test082(),
            None,
        )
