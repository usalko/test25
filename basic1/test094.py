# basic1/test094.py




from typing import List


def test094(input_string: str) -> List[int]:
    '''
    Convert the bytes in a given string to a list of integers.
    '''
    return [int(bytes(x, 'ascii')[0]) for x in input_string]