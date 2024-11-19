from unittest import TestCase

from basic1 import test060


class TestsBasic1Test060(TestCase):
    '''
    Write a Python program to calculate the hypotenuse of a right angled triangle.
    '''

    def test_case1(self):
        self.assertEqual(
            test060(),
            None,
        )
