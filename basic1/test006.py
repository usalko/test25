# basic1/test006.py
from datetime import datetime


def test006(dt: datetime) -> str:
    return dt.isoformat(' ')[0:4+1+2+1+2+1+2+1+2+1+2]