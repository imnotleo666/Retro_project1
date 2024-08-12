"""
This type stub file was generated by pyright.
"""

"""Miscellaneous context managers.
"""
class preserve_keys:
    """Preserve a set of keys in a dictionary.

    Upon entering the context manager the current values of the keys
    will be saved. Upon exiting, the dictionary will be updated to
    restore the original value of the preserved keys. Preserved keys
    which did not exist when entering the context manager will be
    deleted.

    Examples
    --------

    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> with preserve_keys(d, 'b', 'c', 'd'):
    ...     del d['a']
    ...     del d['b']      # will be reset to 2
    ...     d['c'] = None   # will be reset to 3
    ...     d['d'] = 4      # will be deleted
    ...     d['e'] = 5
    ...     print(sorted(d.items()))
    ...
    [('c', None), ('d', 4), ('e', 5)]
    >>> print(sorted(d.items()))
    [('b', 2), ('c', 3), ('e', 5)]
    """
    def __init__(self, dictionary, *keys) -> None:
        ...
    
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, *exc_info): # -> None:
        ...
    


