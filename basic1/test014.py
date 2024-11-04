# basic1/test014.py
from typing import Tuple, List
from calendar import TextCalendar
from datetime import datetime

def test014(input_date1: Tuple[int, int, int], input_date2: Tuple[int, int, int]) -> str:
    return f'{(datetime(*input_date2) - datetime(*input_date1)).days} days'
