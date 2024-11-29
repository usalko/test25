# basic1/test076.py


from sys import argv
from typing import List


def test076() -> List[str]:
    '''
    Get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
    '''
    return [arg for arg in argv]
