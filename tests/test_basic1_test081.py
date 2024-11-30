from unittest import TestCase

from basic1 import test081


class TestsBasic1Test081(TestCase):
    '''
    Write a Python program to concatenate N strings.
    '''

    def test_case1(self):
        self.assertEqual(
            test081('1', '2', 'N'),
            '12N',
        )
