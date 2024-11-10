# basic1/test032.py



def gcd(input_integer1: int, input_integer2: int) -> int:
    if input_integer1 == 0:
        return input_integer2
    if input_integer2 == 0:
        return input_integer1
    rest = input_integer1 % input_integer2
    if rest == 0:
        return input_integer2
    return gcd(input_integer2, rest)

def test032(input_integer1: int, input_integer2: int) -> int:
    if input_integer1 == 0 or input_integer2 == 0:
        return 0
    return (input_integer2 * input_integer1) / gcd(input_integer1, input_integer2)