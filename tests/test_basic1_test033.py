from unittest import TestCase

from basic1 import test033


class TestsBasic1Test033(TestCase):
    '''
    Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
    '''

    def test_case1(self):
        self.assertEqual(
            test033(1, 2, 3), 
            6,
        )
    
    def test_case2(self):
        self.assertEqual(
            test033(2, 2, 3), 
            0,
        )
        
    def test_case3(self):
        self.assertEqual(
            test033(3, 2, 2), 
            0,
        )

    def test_case4(self):
        self.assertEqual(
            test033(2, 3, 2), 
            0,
        )
