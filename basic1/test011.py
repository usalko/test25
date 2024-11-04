# basic1/test011.py
from typing import Callable


def test011(documented_function: Callable) -> str:
    return documented_function.__doc__