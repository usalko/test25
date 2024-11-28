from unittest import TestCase

from basic1 import test086


class TestsBasic1Test086(TestCase):
    '''
    Write a Python program to get the ASCII value of a character.
    '''

    def test_case1(self):
        self.assertEqual(
            test086(),
            None,
        )
