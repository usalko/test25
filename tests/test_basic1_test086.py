from unittest import TestCase

from basic1 import test086


class TestsBasic1Test086(TestCase):
    '''
    Write a Python program to get the ASCII value of a character.
    '''

    def test_case1(self):
        self.assertEqual(
            test086('a'),
            0x61,
        )

    def test_case2(self):
        self.assertEqual(
            test086('b'),
            0x62,
        )
