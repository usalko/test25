# basic1/test075.py


def test075(module) -> str | None:
    '''
    Get the copyright information and write Copyright information in Python code
    '''
    if hasattr(module, '__license__'):
        return module.__license__
    return None