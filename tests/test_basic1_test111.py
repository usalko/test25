from os import popen
from unittest import TestCase

from basic1 import test111


class TestsBasic1Test111(TestCase):
    '''
    Write a Python program to make file lists from the current directory using a wildcard.
    '''

    def test_case1(self):
        entries = [e for a in [[y.strip('\n') for y in x.split('\t')] for x in popen('dir r*').readlines()] for e in a]
        entries.sort()
        self.assertListEqual(
            test111('.', 'r*'),
            entries,
        )
