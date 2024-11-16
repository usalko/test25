# basic1/test047.py


from os import cpu_count


def test047() -> int:
    '''
    Find out the number of CPUs used
    '''
    return cpu_count() or 1
