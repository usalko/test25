# basic1/test103.py


from pathlib import Path


def test103(path: str) -> str:
    '''
    Extract the filename from a given path.
    '''
    return Path(path).name