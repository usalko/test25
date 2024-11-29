# basic1/test077.py


from sys import byteorder


def test077() -> None:
    '''
    Check if system is a big-endian platform
    '''
    return byteorder == 'big'