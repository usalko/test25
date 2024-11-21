from pathlib import Path
from unittest import TestCase

from basic1 import test063


class TestsBasic1Test063(TestCase):
    '''
    Write a Python program to get an absolute file path.
    '''

    def test_case1(self):
        file_name = __file__
        self.assertEqual(
            test063(file_name),
            str(Path(file_name).resolve().absolute()),
        )
