# basic1/test104.py


from os import getegid, geteuid, getgid, getgroups


def test104() -> None:
    '''
    Get the effective group id, effective user id, real group id, and
    a list of supplemental group ids associated with the current process.
    '''
    return getegid(), geteuid(), getgid(), getgroups()