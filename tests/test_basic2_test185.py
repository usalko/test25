from unittest import TestCase

from basic2 import test185


class TestsBasic1Test185(TestCase):
    '''35. Solve Linear Equations

Write a Python program which solve the equation:
ax+by=c
dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.
Input:
a,b,c,d,e,f separated by a single space.
(-1,000 <= a,b,c,d,e,f <= 1,000)
Input the value of a, b, c, d, e, f:
5 8 6 7 9 4
Values of x and y:
-2.000 2.000
    '''

    def test_case1(self):
        self.assertListEqual(
            test185(2),
            0,
        )
