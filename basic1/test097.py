# basic1/test097.py


from sysconfig import get_config_vars
from typing import List


def test097() -> List[str]:
    '''
    List the special variables used in the language.
    '''
    return [str(x) for x in get_config_vars()]