from unittest import TestCase

from basic1 import test067


class TestsBasic1Test067(TestCase):
    '''
    Write a Python program to convert pressure in kilopascals to pounds per square inch,
    a millimeter of mercury (mmHg) and atmosphere pressure.
    '''

    def test_case1(self):
        self.assertEqual(
            test067(),
            None,
        )
