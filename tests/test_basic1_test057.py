from time import time
from unittest import TestCase

from basic1 import test057


class TestsBasic1Test057(TestCase):
    '''
    Write a Python program to get the execution time of a Python method.
    '''

    def test_case1(self):
        def method() -> None:
            for x in range(0, 1999):
                x += 1

        timer0 = time()
        execution_time = test057(method)
        timer0 = time() - timer0
        self.assertTrue(
            execution_time < timer0
        )
