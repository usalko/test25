from os import cpu_count
from unittest import TestCase

from basic1 import test047


class TestsBasic1Test047(TestCase):
    '''
    Write a Python program to find out the number of CPUs used.
    '''

    def test_case1(self):
        self.assertEqual(
            test047(),
            cpu_count(),
        )

