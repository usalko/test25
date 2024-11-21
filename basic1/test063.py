# basic1/test063.py


from os.path import realpath


def test063(file_name: str) -> str:
    '''
    Get an absolute file path.
    '''
    return realpath(file_name)