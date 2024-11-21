# basic1/test061.py


from math import floor
from typing import Tuple

FEET_IN_MILE: int = 1760 * 3
FEET_IN_YARD: int = 3
INCHES_IN_FEET: int = 12

def test061(feet: float) -> Tuple[float, float, float]:
    '''
    Convert the distance (in feet) to inches, yards, and miles.
    1 feet - 12 inches
    1 yard - 3 feet
    1 mile - 1760 yards
    
    @ return tuple (inches, yards, miles)
    '''
    miles = 0
    if feet > FEET_IN_MILE:
        miles = floor(feet / FEET_IN_MILE)
    yards = 0
    if miles > 0:
        yards = floor((feet % FEET_IN_MILE) / FEET_IN_YARD)
    else:
        yards = floor(feet / FEET_IN_YARD)
    inches = 0
    if yards > 0 and miles > 0:
        inches = (feet - miles * FEET_IN_MILE - yards * FEET_IN_YARD) * INCHES_IN_FEET
    elif yards > 0:
        inches = (feet - yards * FEET_IN_YARD) * INCHES_IN_FEET
    else:
        inches = feet * INCHES_IN_FEET
    
    return inches, yards, miles