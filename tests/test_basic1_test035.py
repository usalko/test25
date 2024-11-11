from unittest import TestCase

from basic1 import test035


class TestsBasic1Test035(TestCase):
    '''
    Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
    '''

    def test_case1(self):
        self.assertEqual(
            test035(1, 1, 5),
            True,
        )
    
    def test_case2(self):
        self.assertEqual(
            test035(7, 2, 5),
            True,
        )
    
    def test_case3(self):
        self.assertEqual(
            test035(4, 1, 5),
            True,
        )

    def test_case4(self):
        self.assertEqual(
            test035(2, 1, 5),
            False,
        )

    def test_case5(self):
        self.assertEqual(
            test035(17, 64, 5),
            False,
        )

    def test_case6(self):
        self.assertEqual(
            test035(-999995, 1000000, 5),
            True,
        )
