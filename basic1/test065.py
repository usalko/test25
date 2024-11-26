# basic1/test065.py


from typing import Tuple

SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60


def test065(seconds: int) -> Tuple[int, int, int, int]:
    '''
    Converts seconds into days, hours, minutes, and seconds
    returns Tuple[int, int, int, int] (days, hours, minutes, seconds)
    '''
    days = int(seconds / SECONDS_IN_DAY)
    hours = int((seconds - days * SECONDS_IN_DAY) / SECONDS_IN_HOUR)
    minutes = int((seconds - days * SECONDS_IN_DAY - hours * SECONDS_IN_HOUR) / SECONDS_IN_MINUTE)
    secs = int(seconds - days * SECONDS_IN_DAY - hours * SECONDS_IN_HOUR - minutes * SECONDS_IN_MINUTE)
    return days, hours, minutes, secs