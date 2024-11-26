# basic1/test069.py


from typing import List


def test069(a: int, b: int, c: int) -> List[int]:
    '''
    Sort three integers without using conditional statements and loops
    '''
    result = [a, b, c]
    result.sort()
    return result