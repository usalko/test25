from sysconfig import get_path, get_path_names
from unittest import TestCase

from basic1 import test044


class TestsBasic1Test044(TestCase):
    '''
    Write a Python program to locate Python site packages.
    '''

    def test_case1(self):
        site_types = get_path_names()
        unique_paths = []
        for path in [get_path(site_type) for site_type in site_types]:
            if not path in unique_paths:
                unique_paths.append(path)
        self.assertListEqual(
            test044(),
            unique_paths,
        )

