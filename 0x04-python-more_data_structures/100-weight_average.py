#!/usr/bin/python3


def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    av = 0
    siz = 0
    for t in my_list:
        av += (t[0] * t[1])
        siz += t[1]
    return (av / siz)
