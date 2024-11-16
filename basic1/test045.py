# basic1/test045.py


from os import popen


def test045(external_command: str) -> any:
    '''
    Calls an external command
    '''
    parsed_command = external_command.split(' ')
    if len(parsed_command) < 2 and not parsed_command[0].strip():
        raise BaseException('Sorry, but we are don\'t allow empty command')
    return popen(external_command).readlines()
