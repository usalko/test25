from unittest import TestCase
from basic1 import test015
from datetime import datetime


class TestsBasic1Test015(TestCase):
    '''
Write a Python program to get the volume of a sphere with radius six.
    '''

    def test_case1(self):
        self.assertEqual(
            test015(6),
            904.7786842338603,
        )