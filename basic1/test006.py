# basic1/test006.py
from typing import Tuple, List

def test006(input_string: str) -> Tuple[List[str], Tuple[str]]:
    return (
        list(input_string.split(',')),
        tuple(input_string.split(',')),
    )