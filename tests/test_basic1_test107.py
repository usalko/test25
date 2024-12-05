from unittest import TestCase

from basic1 import test107


class TestsBasic1Test107(TestCase):
    '''
    Write a Python program to retrieve file properties.
    '''

    def test_case1(self):
        self.assertEqual(
            test107(),
            None,
        )
