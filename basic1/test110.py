# basic1/test110.py


from typing import Callable, List


def test110(numbers: List[int], check: Callable[[int], bool]) -> List[int]:
    '''
    Get numbers divisible by fifteen from a list using an anonymous function.
    '''
    return list(filter(check, numbers))