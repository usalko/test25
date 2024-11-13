from unittest import TestCase

from basic1 import test040


class TestsBasic1Test040(TestCase):
    '''
    Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
    '''

    def test_case1(self):
        self.assertEqual(
            test040(),
            None,
        )

