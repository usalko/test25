from unittest import TestCase

from basic1 import test062


class TestsBasic1Test062(TestCase):
    '''
    Write a Python program to convert all units of time into seconds.
    '''

    def test_case1(self):
        self.assertEqual(
            test062(),
            None,
        )
