# basic1/test089.py


def test089(tested_value: int, compared_value: int) -> str | None:
    '''
    Conditional printing if the value is 1, display the string "First day of a Month!"
    and do nothing if the value is not equal.
    '''
    if tested_value == compared_value:
        return 'First day of a Month'