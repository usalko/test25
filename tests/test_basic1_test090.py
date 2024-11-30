from unittest import TestCase

from basic1 import test090


class TestsBasic1Test090(TestCase):
    '''
    Write a Python program to create a copy of its own source code.
    '''

    def test_case1(self):
        self.assertEqual(
            test090(),
            '''# basic1/test090.py


from io import open


def test090() -> str:
    \'''
    Get a copy of its source code
    \'''
    with open(__file__, 'rb') as byte_reader:
        return str(byte_reader.read(), encoding='utf-8')''',
        )
