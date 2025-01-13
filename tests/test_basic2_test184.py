from unittest import TestCase

from basic2 import test184


class TestsBasic1Test184(TestCase):
    '''34. Right Triangle Validator

Write a Python program to check whether three given lengths (integers) of three sides form a right triangle.
Print "Yes" if the given sides form a right triangle otherwise print "No".
Input:
Integers separated by a single space.
1 <= length of the side <= 1,000
Input three integers(sides of a triangle)
8 6 7
No
    '''

    def test_case1(self):
        self.assertListEqual(
            test184(2),
            0,
        )
