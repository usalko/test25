# basic1/test005.py
from datetime import datetime


def test005(dt: datetime) -> str:
    return dt.isoformat(' ')[0:4+1+2+1+2+1+2+1+2+1+2]