from unittest import TestCase

from basic1 import test138


class TestsBasic1Test138(TestCase):
    '''
    Write a Python program to convert true to 1 and false to 0.
    '''

    def test_case1(self):
        self.assertEqual(
            test138(),
            None,
        )
