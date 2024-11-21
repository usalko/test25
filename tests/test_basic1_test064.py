from unittest import TestCase

from basic1 import test064


class TestsBasic1Test064(TestCase):
    '''
    Write a Python program that retrieves the date and time of file creation and modification.
    '''

    def test_case1(self):
        self.assertEqual(
            test064(),
            None,
        )
