from unittest import TestCase

from basic2 import test166


class TestsBasic1Test166(TestCase):
    '''16. Right Triangle Third Side

    Write a Python program to get the third side of a right-angled triangle from two given sides.
    '''

    def test_case1(self):
        self.assertEqual(
            test166(),
            None,
        )
