from unittest import TestCase

from basic1 import test136


class TestsBasic1Test136(TestCase):
    '''
    Extract a single key-value pair from a dictionary into variables.
    '''

    def test_case1(self):
        self.assertEqual(
            test136(),
            None,
        )
