from os import system
from unittest import TestCase

from basic1 import test102


class TestsBasic1Test102(TestCase):
    '''
    Write a Python program to get system command output.
    '''

    def test_case1(self):
        self.assertListEqual(
            test102('cd .'),
            [],
        )

    def test_case2(self):
        self.assertEqual(
            system('cd .'),
            0,
        )
