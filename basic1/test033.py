# basic1/test033.py



def test033(input_integer1: int, input_integer2: int, input_integer3: int) -> int:
    if input_integer1 == input_integer2 or input_integer1 == input_integer3 or input_integer2 == input_integer3:
        return 0
    return input_integer1 + input_integer2 + input_integer3 