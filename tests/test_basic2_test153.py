from unittest import TestCase

from basic2 import test153


class TestsBasic1Test153(TestCase):
    '''3. Remove Every Third

    Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
    '''

    def test_case1(self):
        self.assertEqual(
            test153(),
            None,
        )
