from unittest import TestCase

from basic2 import test163


class TestsBasic1Test163(TestCase):
    '''13. Two-Digit Letter Combos

    Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
    string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
    }
    '''

    def test_case1(self):
        self.assertEqual(
            test163(),
            None,
        )
