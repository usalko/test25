from unittest import TestCase

from basic1 import test076


class TestsBasic1Test076(TestCase):
    '''
    Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
    '''

    def test_case1(self):
        self.assertEqual(
            test076(),
            None,
        )
