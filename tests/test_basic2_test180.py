from unittest import TestCase

from basic2 import test180


class TestsBasic1Test180(TestCase):
    '''30. Palindrome Sum Iteration

Write a Python program to reverse the digits of a given number and add them to the original. Repeat this procedure if the sum is not a palindrome.
Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
    '''

    def test_case1(self):
        self.assertListEqual(
            test180(2),
            0,
        )
