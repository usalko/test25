from unittest import TestCase

from basic2 import test158


class TestsBasic1Test158(TestCase):
    '''8. Google News Top Stories

    Write a Python program that retrieves the top stories from Google News.
    '''

    def test_case1(self):
        self.assertEqual(
            test158(),
            None,
        )
