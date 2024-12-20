from unittest import TestCase

from basic2 import test152


class TestsBasic1Test152(TestCase):
    '''2. All Unique Strings

    Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'.
    Ensure that each character is used only once.
    '''

    def test_case1(self):
        self.assertEqual(
            test152(),
            None,
        )
