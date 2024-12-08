# basic1/test111.py


from os import listdir
from re import Pattern, compile
from typing import List


def convert_wild_card_to_regexp(wild_card: str) -> Pattern:
    result = wild_card.replace('.', '\\.').replace('?', '.').replace('*', '.+')
    return compile(result)

def test111(path: str, wild_card: str) -> List[str]:
    '''
    File lists from the current directory using a wildcard.
    '''
    regular = convert_wild_card_to_regexp(wild_card)
    result = [x for x in listdir(path) if regular.match(x)]
    result.sort()
    return result