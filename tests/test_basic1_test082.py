from unittest import TestCase

from basic1 import test082


class TestsBasic1Test082(TestCase):
    '''
    Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
    '''

    def test_case1(self):
        self.assertEqual(
            test082((1, 2, 3)),
            6,
        )

    def test_case2(self):
        self.assertEqual(
            test082([1, 2, 3]),
            6,
        )

    def test_case3(self):
        self.assertEqual(
            test082({1, 2, 3}),
            6,
        )

    def test_case4(self):
        self.assertEqual(
            test082({'1': 1, '2': 2, '3': 3}),
            6,
        )
