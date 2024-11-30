from unittest import TestCase

from basic1 import test092


class TestsBasic1Test092(TestCase):
    '''
    Write a Python program to define a string containing special characters in various forms.
    '''

    def test_case1(self):
        self.assertEqual(
            test092(),
            None,
        )
