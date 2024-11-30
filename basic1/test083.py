# basic1/test083.py


from typing import List


def test083(input_list: List[int], boundary: int) -> bool:
    '''
    Test whether all numbers in a list are greater than a certain number.
    '''
    result = [x for x in filter(lambda x: x <= boundary, input_list)]
    return len(result) == 0