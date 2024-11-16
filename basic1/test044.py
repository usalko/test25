# basic1/test044.py


from sysconfig import get_paths
from typing import Set


def add_if_missed(container: Set[str], path: str) -> bool:
    if path in container:
        return False
    container.add(path)
    return True

def test044() -> any:
    '''
    Locate Python site packages
    '''
    unique_paths: Set[str] = set()
    return [path for _, path in get_paths().items() if add_if_missed(unique_paths, path)]
