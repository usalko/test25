# basic1/test003.py
from datetime import datetime


def test003(dt: datetime) -> str:
    return dt.isoformat(' ')[0:4+1+2+1+2+1+2+1+2+1+2]