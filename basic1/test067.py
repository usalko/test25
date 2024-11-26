# basic1/test067.py


PASCAL_TO_MMHG = 0.00750062
PASCAL_TO_POUND_PER_SQUARE_INCH = 0.000145038
PASCAL_TO_ATMOSPHERE = 9.86923e-6


def test067(pressure_in_kilo_pascals: float) -> None:
    '''
    Convert pressure in kilopascals to pounds per square inch,
    a millimeter of mercury (mmHg) and atmosphere pressure.
    '''
    pascals = pressure_in_kilo_pascals * 1000.0
    return round(pascals * PASCAL_TO_POUND_PER_SQUARE_INCH, 3),\
        round(pascals * PASCAL_TO_MMHG, 3), \
        round(pascals * PASCAL_TO_ATMOSPHERE, 3)