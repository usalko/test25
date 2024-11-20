# basic1/test057.py


from time import time
from typing import Callable


def test057(method: Callable[[], None]) -> any:
    '''
    Get the execution time of a Python method
    '''
    timer0 = time()
    method()
    return time() - timer0