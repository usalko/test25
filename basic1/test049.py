# basic1/test049.py


from pathlib import Path
from typing import List


def test049(input_string: str) -> List[Path]:
    '''
    List all files in a directory
    '''
    return [path for path in Path(input_string).iterdir()]
