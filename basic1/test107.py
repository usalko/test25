# basic1/test107.py


from os import stat, stat_result


def test107(path: str) -> stat_result:
    '''
    Retrieve file properties.
    '''
    return stat(path, follow_symlinks=True)
