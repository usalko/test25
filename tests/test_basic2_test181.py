from unittest import TestCase

from basic2 import test181


class TestsBasic1Test181(TestCase):
    '''31. Carry Operations Count

Write a Python program to count the number of carry operations for each addition problem.
According to Wikipedia " In elementary arithmetic, a carry is a digit that is transferred
from one column of digits to another column of more significant digits. It is part of the
standard algorithm to add numbers together by starting with the rightmost digits and working
to the left. For example, when 6 and 7 are added to make 13, the "3" is written to the same
column and the "1" is carried to the left".
    '''

    def test_case1(self):
        self.assertListEqual(
            test181(2),
            0,
        )
