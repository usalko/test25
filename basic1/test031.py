# basic1/test031.py



def test031(input_integer1: int, input_integer2: int) -> int:
    if input_integer1 == 0:
        return input_integer2
    if input_integer2 == 0:
        return input_integer1
    rest = input_integer1 % input_integer2
    if rest == 0:
        return input_integer2
    return test031(input_integer2, rest)