from unittest import TestCase
from basic1 import test029
from datetime import datetime


class TestsBasic1Test029(TestCase):
    '''
    Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
    Test Data :
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    Expected Output :
    {'Black', 'White'}
    '''

    def test_case1(self):
        self.assertSetEqual(
            test029(["White", "Black", "Red"], ["Red", "Green"]),
            {'Black', 'White'},
        )