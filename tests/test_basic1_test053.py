from unittest import TestCase

from basic1 import test053


class TestsBasic1Test053(TestCase):
    '''
    Write a Python program to access environment variables.
    '''

    def test_case1(self):
        self.assertEqual(
            test053(),
            None,
        )
