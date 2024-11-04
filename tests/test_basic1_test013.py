from unittest import TestCase
from basic1 import test013
from datetime import datetime


class TestsBasic1Test013(TestCase):
    '''
Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
    '''

    def test_case1(self):
        self.assertEqual(
            test013(''),
            '',
        )