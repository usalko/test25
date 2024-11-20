from unittest import TestCase

from basic1 import test063


class TestsBasic1Test063(TestCase):
    '''
    Write a Python program to get an absolute file path.
    '''

    def test_case1(self):
        self.assertEqual(
            test063(),
            None,
        )
