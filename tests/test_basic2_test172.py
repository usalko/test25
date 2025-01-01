from unittest import TestCase

from basic2 import test172


class TestsBasic1Test172(TestCase):
    '''22. Nth Member of Sequence

Write a Python program to create a sequence where the first four members of the sequence are
equal to one Each successive term of the sequence is equal to the sum of the four previous ones.
Find the Nth member of the sequence.
'''

    def test_case1(self):
        self.assertListEqual(
            test172(2),
            0,
        )
