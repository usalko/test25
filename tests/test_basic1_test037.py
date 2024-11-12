from unittest import TestCase

from basic1 import test037


class TestsBasic1Test037(TestCase):
    '''
    Write a Python program that displays your name, age, and address on three different lines.
    '''

    def test_case1(self):
        self.assertEqual(
            test037("Ivanov Ivan", 50, "St. Petersburg"),
            '''Ivanov Ivan
50
St. Petersburg''',
        )

