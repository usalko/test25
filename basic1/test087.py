# basic1/test087.py


from pathlib import Path


def test087(file_name: str) -> int:
    '''
    Get the size of a file
    '''
    return Path(file_name).stat().st_size