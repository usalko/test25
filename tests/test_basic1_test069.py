from unittest import TestCase

from basic1 import test069


class TestsBasic1Test069(TestCase):
    '''
    Write a Python program to sort three integers without using conditional statements and loops.
    '''

    def test_case1(self):
        self.assertListEqual(
            test069(5, 6, 3),
            [3, 5, 6],
        )
