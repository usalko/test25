# basic1/test024.py

def test024(input_letter: str) -> bool:
    return input_letter[0:1].isalpha() and input_letter[0:1] in 'aeiouy'