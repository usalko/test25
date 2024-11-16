# basic1/test046.py


from pathlib import Path
from typing import Tuple


def test046() -> Tuple[str, str]:
    '''
    Retrieve the path and name of the file currently being executed
    '''
    script_file = Path(__file__).absolute()
    return str(script_file.parent), script_file.name
