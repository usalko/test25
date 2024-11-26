# basic1/test068.py


from functools import reduce


def test068(input_number: int) -> int:
    '''
    Calculate sum of digits of a number
    '''
    return reduce(lambda x, y: x + y, map(lambda x: int(x), [c for c in str(input_number)]))
