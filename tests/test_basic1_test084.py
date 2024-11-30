from unittest import TestCase

from basic1 import test084


class TestsBasic1Test084(TestCase):
    '''
    Write a Python program to count the number of occurrences of a specific character in a string.
    '''

    def test_case1(self):
        self.assertEqual(
            test084('Case sensitive', 'e'),
            3,
        )
