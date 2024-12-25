from unittest import TestCase

from basic2 import test159


class TestsBasic1Test159(TestCase):
    '''9. Locally Installed Modules

    Write a Python program to get a list of locally installed Python modules.
    '''

    def test_case1(self):
        self.assertEqual(
            test159(),
            None,
        )
