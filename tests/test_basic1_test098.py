from unittest import TestCase

from basic1 import test098


class TestsBasic1Test098(TestCase):
    '''
    Write a Python program to get system time.
    
    Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.

    '''

    def test_case1(self):
        self.assertEqual(
            test098(),
            None,
        )
