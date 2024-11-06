# basic1/test018.py

def test018(input_number1: int, input_number2: int, input_number3: int) -> int:
    if input_number1 != input_number2 or input_number1 != input_number3:
        return input_number1 + input_number2 + input_number3
    return input_number1 * 3 ** 2
