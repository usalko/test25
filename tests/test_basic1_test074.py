from unittest import TestCase

from basic1 import test074


class TestsBasic1Test074(TestCase):
    '''
    Write a Python program to hash a word.
    '''

    def test_case1(self):
        self.assertEqual(
            test074(),
            None,
        )
