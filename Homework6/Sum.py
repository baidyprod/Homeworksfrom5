def your_sum(iterable, /, start=0):
    res = 0
    res += start
    for item in iterable:
        res += item
    return res