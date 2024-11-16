from unittest import TestCase

from basic1 import test050


class TestsBasic1Test050(TestCase):
    '''
    Write a Python program to print without a newline or space.
    '''

    def test_case1(self):
        self.assertEqual(
            test050(),
            None,
        )

