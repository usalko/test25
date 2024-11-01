from unittest import TestCase
from basic1 import test005
from datetime import datetime


class TestsBasic1Test005(TestCase):
    '''
    Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
    '''

    def test_case1(self):
        first_name = 'Ivan'
        last_name = 'Usalko'
        self.assertEqual(
            test005(first_name, last_name),
            'Usalko Ivan'
        )