from unittest import TestCase

from basic1 import test071


class TestsBasic1Test071(TestCase):
    '''
    Write a Python program to get a directory listing, sorted by creation date.
    '''

    def test_case1(self):
        self.assertEqual(
            test071(),
            None,
        )
