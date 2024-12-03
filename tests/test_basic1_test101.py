from unittest import TestCase

from basic1 import test101


class TestsBasic1Test101(TestCase):
    '''
    Write a Python program to access and print a URL's content to the console.
    '''

    def test_case1(self):
        self.assertEqual(
            test101(),
            None,
        )
