from unittest import TestCase

from basic2 import test165


class TestsBasic1Test165(TestCase):
    '''15. Operator Priority Checker

    Write a Python program to check the priority of the four operators (+, -, *, /).
    '''

    def test_case1(self):
        self.assertEqual(
            test165(),
            None,
        )
