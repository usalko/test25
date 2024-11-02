# basic1/test008.py
from typing import Tuple, List

def test008(input_string: str) -> Tuple[List[str], Tuple[str]]:
    return (
        list(input_string.split(',')),
        tuple(input_string.split(',')),
    )