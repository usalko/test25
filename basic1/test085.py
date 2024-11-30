# basic1/test085.py


from pathlib import Path
from typing import Literal


def test085(input_file_or_directory_name: str) -> Literal['file', 'directory', 'other']:
    '''
    Check whether a file path is a file or a directory.
    '''
    if Path(input_file_or_directory_name).is_file():
        return 'file'
    if Path(input_file_or_directory_name).is_dir():
        return 'directory'
    return 'other'