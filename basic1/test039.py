# basic1/test039.py


def test039(principal_value: float, rate_of_interest_percents: float, years: int) -> float:
    '''
    The future value formula is FV=PV*(1+r)^n, where PV is the present value of the investment,
    r is the annual interest rate, and n is the number of years the money is invested.
    '''
    return round(principal_value * (1 + rate_of_interest_percents / 100) ** years, 2)