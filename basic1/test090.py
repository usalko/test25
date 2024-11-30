# basic1/test090.py


from io import open


def test090() -> str:
    '''
    Get a copy of its source code
    '''
    with open(__file__, 'rb') as byte_reader:
        return str(byte_reader.read(), encoding='utf-8')