# basic1/test074.py


def test074(word: str) -> int:
    '''
    Hash a word
    '''
    result = 0
    input = bytes(word, 'utf-8')
    rest = len(input) % 4
    if rest > 0:
        input += b'\0' * rest
    for i in range(0, int(len(input) / 4)):
        result += int.from_bytes(input[i:i+4]) * 31
    return result