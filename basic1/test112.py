# basic1/test112.py


from typing import List, TypeVar

A = TypeVar


def test112(input_list: List[A]) -> List[A]:
    '''
    Remove the first item from a specified list.
    '''
    input_list.pop(0)
    return input_list