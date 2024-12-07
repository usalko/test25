# basic1/test102.py


from os import popen


def test102(command: str) -> str:
    '''
    Get system command output.
    '''
    return popen(command).readlines()