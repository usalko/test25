# basic1/test053.py


from os import getenv


def test053(variable_name: str) -> str:
    '''
    Access environment variables
    '''
    return getenv(variable_name)