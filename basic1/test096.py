# basic1/test096.py


from inspect import stack


def test096() -> str:
    '''
    Print the current call stack.
    '''
    return '\n'.join([f'{x.function} {x.filename}:{x.lineno}' for x in stack()])