from sys import modules
from unittest import TestCase

from basic1 import test078


class TestsBasic1Test078(TestCase):
    '''
    Write a Python program to find the available built-in modules.
    '''

    def test_case1(self):
        loaded_builtin_modules = [module_name for module_name, module in modules.items() if 'builtin' in str(module.__loader__).lower()]
        loaded_builtin_modules.sort()
        self.assertTrue(
            set(test078()).issuperset(loaded_builtin_modules),
        )
