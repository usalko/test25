# basic1/test070.py

from pathlib import Path
from typing import List


def test070(files: List[str]) -> List[str]:
    '''
    Sort files by date
    '''
    filepaths = [str(Path(file).absolute().resolve()) for file in files]
    filepaths.sort(key=lambda x: Path(x).lstat().st_ctime)
    filepaths.reverse()
    return filepaths