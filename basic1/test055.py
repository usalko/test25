# basic1/test055.py


from socket import gethostbyname_ex, gethostname
from typing import List


def test055() -> List[str]:
    '''
    Get local IP addresses using Python's stdlib
    '''
    return gethostbyname_ex(gethostname())[2]