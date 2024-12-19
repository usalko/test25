from unittest import TestCase

from basic1 import test139


class TestsBasic1Test139(TestCase):
    '''
    Write a Python program to validate an IP address.
    '''

    def test_case1(self):
        self.assertEqual(
            test139(),
            None,
        )
