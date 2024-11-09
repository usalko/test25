# basic1/test029.py

from typing import List, Set


def test029(list1: List[str], list2: List[str]) -> Set[str]:
    return set(list1) - set(list2)
