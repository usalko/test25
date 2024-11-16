from os import popen
from unittest import TestCase

from basic1 import test045


class TestsBasic1Test045(TestCase):
    '''
    Write a Python program that calls an external command.
    '''

    def test_case1(self):
        self.assertListEqual(
            test045('dir .'),
            popen('dir .').readlines(),
        )

