# basic1/test040.py


from math import sqrt
from typing import Tuple


def test040(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    '''
    Calculate the distance between the points (x1, y1) and (x2, y2).
    '''
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)