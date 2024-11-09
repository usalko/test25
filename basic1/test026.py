# basic1/test026.py

from typing import List


def test026(input_list: List[int]) -> str:
    result = ''
    for i in input_list:
        result += '*' * i + '\n'
    return result