from unittest import TestCase
from basic1 import test007
from datetime import datetime


class TestsBasic1Test007(TestCase):
    '''
    Write a Python program that accepts a filename from the user and prints the extension of the file.
    Sample filename : abc.java
    Output : java
    '''

    def test_case1(self):
        self.assertEqual(
            test007('abc.java'),
            'java',
        )
