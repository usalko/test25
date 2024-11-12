from unittest import TestCase

from basic1 import test038


class TestsBasic1Test038(TestCase):
    '''
    Write a Python program to solve (x + y) * (x + y).
    Test Data : x = 4, y = 3
    Expected Output : (4 + 3) ^ 2) = 49
    '''

    def test_case1(self):
        self.assertEqual(
            test038(4, 3),
            '(4 + 3) ^ 2 = 49',
        )

