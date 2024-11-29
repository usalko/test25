from unittest import TestCase

from basic1 import test076
from sys import orig_argv


class TestsBasic1Test076(TestCase):
    '''
    Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
    '''

    def test_case1(self):
        args = test076()
        self.assertListEqual(
            test076(),
            orig_argv[-len(args):],
        )
