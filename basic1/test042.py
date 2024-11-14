# basic1/test042.py


from platform import architecture


def test042() -> any:
    '''
    determine if a Python shell is executing in 32bit or 64bit mode on O
    '''
    return int(architecture()[0][0:2])