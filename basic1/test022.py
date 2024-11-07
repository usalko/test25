# basic1/test022.py

from functools import reduce
from typing import List


def test022(input_list_of_number: List[int], input_number: int) -> int:
    return reduce(lambda x, y:  x + 1 if y == input_number else x, input_list_of_number, 0)