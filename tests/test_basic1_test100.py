from unittest import TestCase

from basic1 import test100


class TestsBasic1Test100(TestCase):
    '''
    Write a Python program to get the name of the host on which the routine is running.
    '''

    def test_case1(self):
        self.assertEqual(
            test100(),
            None,
        )
