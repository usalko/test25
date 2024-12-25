from unittest import TestCase

from basic2 import test157


class TestsBasic1Test157(TestCase):
    '''7. Character Frequency in File

    Write a Python program to count the number of each character in a text file.
    '''

    def test_case1(self):
        self.assertEqual(
            test157(),
            None,
        )
