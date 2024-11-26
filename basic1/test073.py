# basic1/test073.py


from typing import Tuple


def test073(point1: Tuple[float, float], point2: Tuple[float, float]) -> Tuple[float, float]:
    '''
    Calculate the midpoints of a line
    '''
    return point1[0] + (point2[0] - point1[0]) / 2, point1[1] + (point2[1] - point1[1]) / 2