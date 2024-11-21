# basic1/test062.py


SECONDS_IN_WEEK = 7 * 24 * 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60


def test062(weeks: int, days: int, hours: int, minutes: int) -> float:
    '''
    Convert week, day, hour, minute of time into seconds
    '''
    return weeks * SECONDS_IN_WEEK + days * SECONDS_IN_DAY + hours * SECONDS_IN_HOUR + minutes * SECONDS_IN_MINUTE