# basic1/test056.py


from shutil import get_terminal_size


def test056() -> any:
    '''
    Get the height and width of the console window
    '''
    return get_terminal_size()