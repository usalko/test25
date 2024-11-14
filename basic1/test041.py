# basic1/test041.py


from pathlib import Path


def test041(file_name: str) -> any:
    '''
    Check whether a file exists.
    '''
    return Path.exists(Path.absolute(Path(file_name)))