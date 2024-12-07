from unittest import TestCase

from basic1 import test108


class TestsBasic1Test108(TestCase):
    '''
    Write a Python program to find the path to a file or directory when you encounter a path name.
    '''

    def test_case1(self):
        self.assertEqual(
            test108('This is the path to temp folder /tmp isn\'t it?'),
            '/tmp',
        )
