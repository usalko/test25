from unittest import TestCase

from basic1 import test074


class TestsBasic1Test074(TestCase):
    '''
    Write a Python program to hash a word.
    '''

    def test_case1(self):
        self.assertEqual(
            test074('This'),
            43899995373,
        )

    def test_case2(self):
        self.assertEqual(
            test074('That'),
            43899931916,
        )

    def test_case3(self):
        self.assertEqual(
            test074('Those'),
            43900042989,
        )
