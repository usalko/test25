# basic1/test016.py

def test016(input_number1: int, input_number2: int) -> int:
    if input_number1 <= input_number2:
        return input_number1 - input_number2
    return abs(input_number1 - input_number2) * 2
