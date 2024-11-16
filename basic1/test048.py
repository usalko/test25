# basic1/test048.py


def test048(input_string: str) -> any:
    '''
    Parse a string to float or integer.
    '''
    try:
        if '.' in input_string:
            return float(input_string)
    except:
        pass
    return int(input_string)
