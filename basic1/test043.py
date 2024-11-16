# basic1/test043.py


from os import name
from sys import platform, version_info


def test043() -> any:
    '''
    Get OS name, platform and release information.
    '''
    version = f'{version_info.minor}.{version_info.micro}-{version_info.releaselevel}-{version_info.serial}'
    return f'{name}, {platform}, {version_info.major}.{version}'
