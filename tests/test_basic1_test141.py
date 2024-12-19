from unittest import TestCase

from basic1 import test141


class TestsBasic1Test141(TestCase):
    '''
    Write a python program to convert decimal to hexadecimal.
    Sample decimal number: 30, 4
    Expected output: 1e, 04
    '''

    def test_case1(self):
        self.assertEqual(
            test141(),
            None,
        )
