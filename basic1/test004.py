# basic1/test004.py
from math import pi

def test004(circle_radius: float) -> str:
    return f'''
r = {circle_radius}
Area = {pi * (circle_radius * circle_radius)}
'''