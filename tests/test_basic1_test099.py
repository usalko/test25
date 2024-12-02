from unittest import TestCase

from basic1 import test099


class TestsBasic1Test099(TestCase):
    '''
    Write a Python program to clear the screen or terminal.
    '''

    def test_case1(self):
        self.assertEqual(
            test099(),
            0,
        )
