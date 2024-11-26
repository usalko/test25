from os import remove, removedirs
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import List, Tuple
from unittest import TestCase

from basic1 import test070


class TestsBasic1Test070(TestCase):
    '''
    Write a Python program to sort files by date.
    '''
    
    def create_tmp_files(self, dir_prefix: str) -> Tuple[str, List[str]]:
        tmpdir_name = ''
        with TemporaryDirectory(prefix=dir_prefix, delete=False) as tmpdir:
            tmpdir_name = tmpdir

        sorted_by_creation_time_filenames = []
        for name in ['Z', 'Q', 'A']:
            filename = ''
            with NamedTemporaryFile(dir=tmpdir_name, prefix=name, suffix='.txt', delete_on_close=False, delete=False) as writer:
                writer.write(b' ')
                filename = writer.name
            sorted_by_creation_time_filenames.append(str(Path(filename).absolute().resolve()))

        return tmpdir_name, sorted_by_creation_time_filenames

    def test_case1(self):
        folder, sorted_absolute_filenames = self.create_tmp_files('test070')
        
        try:
            self.assertListEqual(
                test070(folder),
                sorted_absolute_filenames,
            )
        finally:
            for filename in sorted_absolute_filenames:
                remove(filename)
            removedirs(folder)
