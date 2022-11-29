def your_enumerate(iterable, start=0):
    res = list(zip(range(start, start + len(iterable)), iterable))
    return res

print(list(enumerate('1234567890', 1)) == your_enumerate('1234567890', 1))