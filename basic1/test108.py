# basic1/test108.py


from re import compile


def test108(text: str) -> str:
    '''
    Find the path to a file or directory when you encounter a path name.
    '''
    for match in compile(r'((/[^/ ]*)+)').finditer(text):
        return match.group(1)
    return None