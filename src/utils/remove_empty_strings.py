from collections.abc import Iterable


def remove_empty_strings(iterable: Iterable):
    """Takes an iterable and returns a list where any empty string has been removed."""

    return list(filter(lambda x: x != "", iterable))
