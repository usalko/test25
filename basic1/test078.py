# basic1/test078.py


from sys import builtin_module_names


def test078() -> None:
    '''
    Find the available built-in modules
    '''
    return [module_name for module_name in builtin_module_names]