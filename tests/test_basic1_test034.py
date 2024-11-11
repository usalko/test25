from unittest import TestCase

from basic1 import test034


class TestsBasic1Test034(TestCase):
    '''
    Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
    '''

    def test_case1(self):
        self.assertEqual(
            test034(1, 2), 
            3,
        )

    def test_case2(self):
        self.assertEqual(
            test034(17, 2), 
            20,
        )
    
