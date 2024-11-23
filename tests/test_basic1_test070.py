from unittest import TestCase

from basic1 import test070


class TestsBasic1Test070(TestCase):
    '''
    Write a Python program to sort files by date.
    '''

    def test_case1(self):
        self.assertEqual(
            test070(),
            None,
        )
