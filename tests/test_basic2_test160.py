from unittest import TestCase

from basic2 import test160


class TestsBasic1Test160(TestCase):
    '''10. OS Information Display

    Write a Python program to display some information about the OS where the script is running.
    '''

    def test_case1(self):
        self.assertEqual(
            test160(),
            None,
        )
