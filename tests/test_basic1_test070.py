from os import remove, removedirs
from pathlib import Path
from random import randint
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import List, Tuple
from unittest import TestCase

from basic1 import test070


class TestsBasic1Test070(TestCase):
    '''
    Write a Python program to sort files by date.
    '''
    
    @staticmethod
    def create_tmp_files(dir_prefix: str) -> Tuple[str, List[str]]:
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
    
    @staticmethod
    def randomize(input: List[str]) -> None:
        if len(input) < 2:
            return
        for i in range(0, int(len(input) / 2)):
            j = randint(0, len(input) - 1)
            while i == j:
                j = randint(0, len(input) - 1)
            value_i = input[i]
            input[i] = input[j]
            input[j] = value_i
            

    def assertListNotEqual(self, list_a: List[str], list_b: List[str]) -> None:
        if len(list_a) != len(list_b):
            return
        for i in range(0, len(list_a)):
            if list_a[i] != list_b[i]:
                return
        self.assertTrue(False)

    def test_case1(self):
        folder, sorted_absolute_filenames = self.create_tmp_files('test070')
        input_filenames = [file_name for file_name in sorted_absolute_filenames]
        self.randomize(input_filenames)
        
        try:
            self.assertListNotEqual(
                input_filenames,
                sorted_absolute_filenames,
            )

            self.assertListEqual(
                test070(input_filenames),
                sorted_absolute_filenames,
            )
        finally:
            for filename in sorted_absolute_filenames:
                remove(filename)
            removedirs(folder)
