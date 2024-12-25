from unittest import TestCase

from basic2 import test156


class TestsBasic1Test156(TestCase):
    '''6. Word Frequency Counter

    Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.
    '''

    def test_case1(self):
        self.assertEqual(
            test156(),
            None,
        )
