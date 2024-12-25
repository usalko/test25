from unittest import TestCase

from basic2 import test161


class TestsBasic1Test161(TestCase):
    '''11. Three Array Sum Combinations

    Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value.
    Print all those three-element combinations.
    Sample data:
    /*
    X = [10, 20, 20, 20]
    Y = [10, 20, 30, 40]
    Z = [10, 30, 40, 20]
    target = 70
    */
    '''

    def test_case1(self):
        self.assertEqual(
            test161(),
            None,
        )
