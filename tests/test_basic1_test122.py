from unittest import TestCase

from basic1 import test122


class TestsBasic1Test122(TestCase):
    '''
    Write a Python program to empty a variable without destroying it.

    Sample data: n=20
    d = {"x":200}
    Expected Output : 0
    {}

    '''

    def test_case1(self):
        self.assertEqual(
            test122(),
            None,
        )
