# basic1/test012.py
from typing import Tuple, List

def test012(exam_st_date: Tuple[int, int, int]) -> str:
    return f'The examination will start from : {exam_st_date[0]:02d} / {exam_st_date[1]:02d} / {exam_st_date[2]:04d}'