from os import remove
from tempfile import NamedTemporaryFile
from unittest import TestCase

from basic1 import test087


class TestsBasic1Test087(TestCase):
    '''
    Write a Python program to get the size of a file.
    '''
    
    @staticmethod
    def create_tmp_file(file_prefix: str, content: bytes) -> str:
        with NamedTemporaryFile(prefix=file_prefix, suffix='.txt', delete_on_close=False, delete=False) as writer:
            writer.write(content)
            return writer.name

    def test_case1(self):
        tmp_file_name = self.create_tmp_file('test087', b'12')
        try:
            self.assertEqual(
                test087(tmp_file_name),
                2,
            )
        finally:
            remove(tmp_file_name)
