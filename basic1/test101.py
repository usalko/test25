# basic1/test101.py


from http.client import HTTPResponse
from urllib.request import urlopen


def test101(url: str) -> str:
    '''
    Get URL's content.
    '''
    response: HTTPResponse = urlopen(url)
    return str(response.read1(), encoding='utf-8')