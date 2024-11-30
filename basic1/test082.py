# basic1/test082.py


from functools import reduce
from typing import Dict, List, Set, Tuple


def test082(container: Tuple[int] | List[int] | Set[int] | Dict[any, int]) -> int:
    '''
    Calculate the sum of all items of a container (tuple, list, set, dictionary).
    '''
    if type(container) == List or type(container) == list or \
        type(container) == Tuple or type(container) == tuple or\
            type(container) == Set or type(container) == set:
        return reduce(lambda x, y: x + y, container)
    if type(container) == Dict or type(container) == dict:
        return reduce(lambda x, y: x + y, container.values())
    return 0