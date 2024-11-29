# basic1/test079.py


from sys import getsizeof


def test079(obj: any) -> int:
    '''
    Get the size of an object in bytes
    '''
    return getsizeof(obj)