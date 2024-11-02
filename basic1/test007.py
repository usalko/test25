# basic1/test007.py
from typing import Tuple, List

def test007(input_string: str) -> Tuple[List[str], Tuple[str]]:
    return (
        list(input_string.split(',')),
        tuple(input_string.split(',')),
    )