# basic1/test109.py

from typing import Literal

NUMBER_TYPE = Literal['positive', 'negative', 'zero']

def test109(number: int) -> NUMBER_TYPE:
    '''
    Check if a number is positive, negative or zero.
    '''
    if number < 0:
        return 'negative'
    if number > 0:
        return 'positive'
    return 'zero'