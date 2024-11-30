from string import punctuation
from unittest import TestCase

from basic1 import test092


class TestsBasic1Test092(TestCase):
    '''
    Write a Python program to define a string containing special characters in various forms.
    '''
    # TODO: consider how to test that:
    # Print a string containing special characters without escaping.
    # print()
    # print("\#{'}${\"}@/")

    # # Print a string containing special characters with escaped single quotes.
    # print("\#{'}${\"}@/")

    # # Print a raw string using triple-quotes with special characters.
    # print(r"""\#{'}${"}@/""")

    # # Print a string containing special characters without escaping.
    # print('\#{\'}${"}@/')

    # # Print a string containing special characters with escaped single quotes.
    # print('\#{'"'"'}${"}@/')

    # # Print a raw string using triple-quotes with special characters.
    # print(r'''\#{'}${"}@/''')
    # print()

    def test_case1(self):
        for special_character in punctuation:
            self.assertEqual(
                test092(special_character, '\\'),
                '\\' + special_character,
            )
