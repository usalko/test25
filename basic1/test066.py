# basic1/test066.py


def test066(body_weight_in_kg: float, body_height_in_cm: float) -> float:
    '''
    Calculate the body mass index
    '''
    return round(body_weight_in_kg / ((body_height_in_cm / 100) ** 2), 1)