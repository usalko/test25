# basic1/test019.py

def test019(input_string: str) -> str:
    return 'Is' + input_string if not input_string.startswith('Is') else input_string
