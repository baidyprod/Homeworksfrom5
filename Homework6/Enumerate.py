def your_enumerate(iterable, start=0):
    res = list(zip(range(start, start + len(iterable)), iterable))
    return res