# basic1/test100.py


from socket import gethostname


def test100() -> None:
    '''
    Get the name of the host on which the routine is running.
    '''
    return gethostname()