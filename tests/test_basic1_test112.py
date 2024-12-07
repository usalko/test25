from unittest import TestCase

from basic1 import test112


class TestsBasic1Test112(TestCase):
    '''
    Write a Python program to remove the first item from a specified list.
    '''

    def test_case1(self):
        self.assertEqual(
            test112(),
            None,
        )
