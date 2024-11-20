from os import get_terminal_size
from shutil import get_terminal_size as shutil_get_terminal_size
from sys import stdout
from unittest import TestCase

from basic1 import test056


class TestsBasic1Test056(TestCase):
    '''
    Write a Python program to get the height and width of the console window.
    '''

    def test_case1(self):
        try:
            terminal_size = get_terminal_size(stdout.fileno())
        except OSError:
            terminal_size = shutil_get_terminal_size()
        self.assertEqual(
            test056(),
            terminal_size,
        )
