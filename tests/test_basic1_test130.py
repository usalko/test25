from unittest import TestCase

from basic1 import test130


class TestsBasic1Test130(TestCase):
    '''
    Write a Python program that uses double quotes to display strings.
    '''

    def test_case1(self):
        self.assertEqual(
            test130(),
            None,
        )
