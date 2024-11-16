from os import name
from sys import platform, version_info
from unittest import TestCase

from basic1 import test043


class TestsBasic1Test043(TestCase):
    '''
    Write a Python program to get OS name, platform and release information.
    '''

    def test_case1(self):
        info = f'{name}, {platform}, {version_info.major}.{version_info.minor}.{version_info.micro}-{version_info.releaselevel}-{version_info.serial}'
        self.assertEqual(
            test043(),
            info,
        )

