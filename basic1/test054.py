# basic1/test054.py


from getpass import getuser


def test054() -> str:
    '''
    Get the current username
    '''
    return getuser()