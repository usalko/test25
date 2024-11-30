# basic1/test093.py


from typing import Tuple, Type


def test093(obj: any) -> Tuple[int, Type, any]:
    '''
    Get Identity, Type, and Value of an object
    '''
    return id(obj), type(obj), obj
