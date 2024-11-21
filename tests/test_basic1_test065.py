from unittest import TestCase

from basic1 import test065


class TestsBasic1Test065(TestCase):
    '''
    Write a Python program that converts seconds into days, hours, minutes, and seconds.
    '''

    def test_case1(self):
        self.assertEqual(
            test065(),
            None,
        )
