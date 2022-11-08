def your_enumerate(iterable, start=0):
    indexes = list(range(start, start+len(iterable)))
    res = list(zip(indexes, iterable))
    return res