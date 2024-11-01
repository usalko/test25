# basic1/test001.py

def test001(input_string: str) -> str:
    result = ''
    maximal_margin_in_spaces = 8
    current_margin_in_spaces = 4
    for word in input_string.split(' '):
        # detect events
        if word == word.capitalize() and len(result) > 0 and len(word) > 1:
            # new line before
            current_margin_in_spaces = min(current_margin_in_spaces, maximal_margin_in_spaces)
            result = result[0:-1] + '\n' + current_margin_in_spaces * ' '
            current_margin_in_spaces += 4
            
        if word.endswith('.'):
            # new paragraph
            current_margin_in_spaces = 0
            
        result += word + ' '
        
    return result[0:-1]