from unittest import TestCase

from basic1 import test046


class TestsBasic1Test046(TestCase):
    '''
    Write a Python program to retrieve the path and name of the file currently being executed.
    '''

    def test_case1(self):
        self.assertEqual(
            test046(),
            None,
        )

