# basic1/test099.py


from os import popen


def test099() -> None:
    '''
    Clear the screen or terminal.
    '''
    try:
        with popen('clear') as p:
            p.readlines()
            return 0
    except:
        return 1