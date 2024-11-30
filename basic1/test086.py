# basic1/test086.py


def test086(character: str) -> int:
    '''
    Get the ASCII value of a character.
    '''
    if len(character) == 0:
        raise 'Input character should be a string with length greater then zero'
    if not character[0].encode('ascii').isascii():
        raise 'Input character not ascii'
    return int(character[0].encode('ascii')[0])