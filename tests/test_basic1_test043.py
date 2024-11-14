from unittest import TestCase

from basic1 import test043


class TestsBasic1Test043(TestCase):
    '''
    Write a Python program to get OS name, platform and release information.
    '''

    def test_case1(self):
        self.assertEqual(
            test043(),
            None,
        )

