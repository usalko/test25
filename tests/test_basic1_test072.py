from unittest import TestCase

from basic1 import test072


class TestsBasic1Test072(TestCase):
    '''
    Write a Python program to get the details of the math module.
    '''

    def test_case1(self):
        import math
        
        self.assertEqual(
            test072(math),
            dir(math),
        )
