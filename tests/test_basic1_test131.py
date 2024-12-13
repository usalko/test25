from unittest import TestCase

from basic1 import test131


class TestsBasic1Test131(TestCase):
    '''
    Write a Python program to split a variable length string into variables.
    '''

    def test_case1(self):
        self.assertEqual(
            test131(),
            None,
        )
