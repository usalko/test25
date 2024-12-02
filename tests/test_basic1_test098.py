from os import times
from time import time_ns
from unittest import TestCase

from basic1 import test098v1, test098v2


class TestsBasic1Test098(TestCase):
    '''
    Write a Python program to get system time.
    
    Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.

    '''

    def test_case1(self):
        system_time = times()[1]
        self.assertTrue(
            system_time <= test098v1()
        )

    def test_case2(self):
        system_time = time_ns()
        self.assertTrue(
            system_time <= test098v2()
        )
