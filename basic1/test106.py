# basic1/test106.py


from typing import List


def test106(path: str) -> List[str]:
    '''
    Divide a path by the extension separator
    '''
    return path.rsplit('.', 1)