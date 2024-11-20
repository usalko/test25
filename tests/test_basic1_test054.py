from os import popen
from sys import platform
from unittest import TestCase

from basic1 import test054


class TestsBasic1Test054(TestCase):
    '''
    Write a Python program to get the current username.
    '''

    def test_case1(self):
        username = ''
        if platform == "win32": # TODO: fix for windows
            username = popen('whoami').readline().strip('\n')
        else:
            username = popen('whoami').readline().strip('\n')
            
        self.assertEqual(
            test054(),
            username,
        )
