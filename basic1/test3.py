# basic1/test3.py
from datetime import datetime


def test3(dt: datetime) -> str:
    return dt.isoformat(' ')[0:4+1+2+1+2+1+2+1+2+1+2]