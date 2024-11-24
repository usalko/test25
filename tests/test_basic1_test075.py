from unittest import TestCase

from basic1 import test075


class TestsBasic1Test075(TestCase):
    '''
    Write a Python program to get the copyright information and write Copyright information in Python code.
    '''

    def test_case1(self):
        self.assertEqual(
            test075(),
            None,
        )
