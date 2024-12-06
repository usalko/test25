from unittest import TestCase

from basic1 import test109


class TestsBasic1Test109(TestCase):
    '''
    Check if a number is positive, negative or zero.
    '''

    def test_case1(self):
        self.assertEqual(
            test109(),
            None,
        )
