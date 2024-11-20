# basic1/test052.py


def test052(text: str) -> None:
    '''
    Print to STDERR
    '''
    import sys
    print(text, file=sys.stderr)