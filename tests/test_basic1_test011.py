from unittest import TestCase
from basic1 import test011
from datetime import datetime


class TestsBasic1Test011(TestCase):
    '''
    Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
    Sample function : abs()
    Expected Result :
    abs(number) -> number
    Return the absolute value of the argument.
    '''

    def test_case1(self):
        self.assertEqual(
            test011(abs),
            'Return the absolute value of the argument.',
        )