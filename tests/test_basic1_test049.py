from os import popen
from pathlib import Path
from re import split
from unittest import TestCase

from basic1 import test049


class TestsBasic1Test049(TestCase):
    '''
    Write a Python program to list all files in a directory.
    '''

    def test_case1(self):
        dir_output = map(lambda output_line: split(
            r'\s+', output_line.strip(' \n\t')), popen('dir ..').readlines())
        dir_output = [Path('..', x) for y in dir_output for x in y]
        self.assertListEqual(
            sorted(test049('..')),
            sorted(dir_output),
        )
