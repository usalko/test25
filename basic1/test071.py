# basic1/test070.py

from os import listdir
from pathlib import Path
from typing import List


def test071(dirname: str) -> List[str]:
    '''
    Get a directory listing, sorted by creation date.
    '''
    filepaths = listdir(dirname)
    filepaths.sort(key=lambda x: Path(dirname, x).lstat().st_ctime)
    return [str(Path(dirname, filename).absolute().resolve()) for filename in filepaths]