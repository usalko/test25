# basic1/test098.py


from os import times
from time import time_ns


def test098v1() -> None:
    '''
    Get system time.
    '''
    return times()[1]

def test098v2() -> None:
    '''
    Get system time.
    '''
    return time_ns()