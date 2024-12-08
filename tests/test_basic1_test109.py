from unittest import TestCase

from basic1 import test109


class TestsBasic1Test109(TestCase):
    '''
    Check if a number is positive, negative or zero.
    '''

    def test_case1(self):
        self.assertEqual(
            test109(-3),
            'negative',
        )

    def test_case2(self):
        self.assertEqual(
            test109(3),
            'positive',
        )

    def test_case3(self):
        self.assertEqual(
            test109(0),
            'zero',
        )
