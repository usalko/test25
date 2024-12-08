# basic1/test114.py


from typing import List


def test114(input_list: List[int]) -> List[int]:
    '''
    Filter positive numbers from a list.
    '''
    return [x for x in filter(lambda x: x >= 0, input_list)]