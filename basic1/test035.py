# basic1/test035.py


def test035(input_integer1: int, input_integer2: int, boundary: int) -> bool:
    return input_integer1 == input_integer2 or \
        input_integer1 - input_integer2 == boundary or \
        input_integer2 - input_integer1 == boundary or \
        input_integer1 + input_integer2 == boundary
