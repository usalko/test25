from unittest import TestCase

from basic1 import test051


class TestsBasic1Test051(TestCase):
    '''
    Write a Python program to determine the profiling of Python programs.
    Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
    These statistics can be formatted into reports via the pstats module.
    '''

    def test_case1(self):
        self.assertEqual(
            test051(),
            None,
        )

