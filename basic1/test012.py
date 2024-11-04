# basic1/test012.py
from typing import Tuple, List
from calendar import TextCalendar

def test012(month: int, year: int) -> str:
    return TextCalendar().formatmonth(year, month)
