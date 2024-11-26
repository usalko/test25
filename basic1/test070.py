# basic1/test070.py

from os import listdir
from pathlib import Path


def test070(dirname: str) -> None:
    '''
    Sort files by date
    '''
    filepaths = listdir(dirname)
    filepaths.sort(key=lambda x: Path(dirname, x).lstat().st_ctime)
    filepaths.reverse()
    return [str(Path(dirname, filename).absolute().resolve()) for filename in filepaths]