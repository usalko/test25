from unittest import TestCase

from basic1 import test091


class TestsBasic1Test093(TestCase):
    '''
    Write a Python program to swap two variables.
    '''

    def test_case1(self):
        var1 = '1'
        var2 = '2'
        self.assertTupleEqual(
            test091((var1, var2)),
            ('2', '1'),
        )
