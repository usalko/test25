# basic1/test105.py


from os import environ


def test105() -> None:
    '''
    Get the users environment.
    '''
    return environ.get('USER')