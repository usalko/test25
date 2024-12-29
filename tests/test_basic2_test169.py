from unittest import TestCase

from basic2 import test169


class TestsBasic1Test169(TestCase):
    '''19. Sequential Powers of Two

Write a Python program that finds the value of n when n degrees of number 2 are
written sequentially on a line without spaces between them.
'''

    def test_case1(self):
        self.assertListEqual(
            test169(2),
            [11, 69, 88, 96],
        )
