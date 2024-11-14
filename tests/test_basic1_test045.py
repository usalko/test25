from unittest import TestCase

from basic1 import test045


class TestsBasic1Test045(TestCase):
    '''
    Write a Python program that calls an external command.
    '''

    def test_case1(self):
        self.assertEqual(
            test045(),
            None,
        )

