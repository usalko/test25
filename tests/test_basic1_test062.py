from unittest import TestCase

from basic1 import test062


class TestsBasic1Test062(TestCase):
    '''
    Write a Python program to convert all (stable) units of time into seconds.
    '''

    def test_case1(self):
        self.assertEqual(
            test062(1, 1, 1, 1),
            694860,
        )

    def test_case2(self):
        self.assertEqual(
            test062(2, 2, 2, 2),
            1389720,
        )
