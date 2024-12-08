# basic1/test113.py


class NotANumberException(BaseException):
    pass


def test113(input_number: int) -> bool:
    '''
    Check inputs a number and generates an error message if it is not a number
    '''
    if type(input_number) == int:
        return True
    if type(input_number) == float:
        return True
    raise NotANumberException