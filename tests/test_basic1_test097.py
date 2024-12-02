from sysconfig import get_config_vars
from unittest import TestCase

from basic1 import test097


class TestsBasic1Test097(TestCase):
    '''
    Write a Python program to list the special variables used in the language.
    '''

    def test_case1(self):
        self.assertListEqual(
            test097(),
            list(get_config_vars().keys()),
        )
