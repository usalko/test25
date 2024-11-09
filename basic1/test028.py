# basic1/test028.py

from typing import List


def test028(input_array: List[int], break_number: int) -> str:
    filtered = []
    for x in input_array:
        if x == break_number:
            break
        if x % 2 == 0:
            filtered.append(x)
    return ' '.join(map(str, filtered))