from unittest import TestCase

from basic1 import test056


class TestsBasic1Test056(TestCase):
    '''
    Write a Python program to get the height and width of the console window.
    '''

    def test_case1(self):
        self.assertEqual(
            test056(),
            None,
        )
