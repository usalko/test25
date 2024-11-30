from os import remove, rmdir
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest import TestCase

from basic1 import test085


class TestsBasic1Test085(TestCase):
    '''
    Write a Python program to check whether a file path is a file or a directory.
    '''

    @staticmethod
    def create_tmp_folder(dir_prefix: str) -> str:
        with TemporaryDirectory(prefix=dir_prefix, delete=False) as tmpdir:
            return tmpdir

    @staticmethod
    def create_tmp_file(file_prefix: str) -> str:
        with NamedTemporaryFile(prefix=file_prefix, suffix='.txt', delete_on_close=False, delete=False) as writer:
            writer.write(b' ')
            return writer.name

    def test_case1(self):
        tmp_file_name = self.create_tmp_file('test085')
        try:
            self.assertEqual(
                test085(tmp_file_name),
                'file',
            )
        finally:
            remove(tmp_file_name)

    def test_case2(self):
        tmp_folder_name = self.create_tmp_folder('test085')
        try:
            self.assertEqual(
                test085(tmp_folder_name),
                'directory',
            )
        finally:
            rmdir(tmp_folder_name)
