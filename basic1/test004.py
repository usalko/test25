# basic1/test004.py
from datetime import datetime


def test004(dt: datetime) -> str:
    return dt.isoformat(' ')[0:4+1+2+1+2+1+2+1+2+1+2]