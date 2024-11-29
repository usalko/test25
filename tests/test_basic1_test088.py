from unittest import TestCase

from basic1 import test088


class TestsBasic1Test088(TestCase):
    '''
    Given variables x=30 and y=20, write a Python program to print "30+20=50".
    '''

    def test_case1(self):
        self.assertEqual(
            test088(),
            None,
        )
