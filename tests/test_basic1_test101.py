from unittest import TestCase

from basic1 import test101


class TestsBasic1Test101(TestCase):
    '''
    Write a Python program to access and print a URL's content to the console.
    '''

    def test_case1(self):
        content = test101('https://google.com')
        self.assertTrue(
            '<html' in content,
        )
