def your_range(a:int, b:int=None, c:int=None) -> list:
    '''
    Returns a list of integers in such way:
    range(stop) - default start value = 0, default step value = 1
    range(start, stop) - default step value = 1
    range(start, stop, step)
    '''
    if b is None and c is None:
        start = 0
        stop = a
        step = 1
    elif c is None:
        start = a
        stop = b
        step = 1
    else:
        start = a
        stop = b
        step = c
    res = []
    if start < stop:
        while start < stop:
            res.append(start)
            start += step
    else:
        while start > stop:
            res.append(start)
            start += step
    return res

print(list(range(10)) == your_range(10))
print(list(range(10, 20)) == your_range(10, 20))
print(list(range(10, 20, 3)) == your_range(10, 20, 3))
print(list(range(20, 10, 3)) == your_range(20, 10, 3))
print(list(range(20, 10, -3)) == your_range(20, 10, -3))
print(list(range(20, 10)) == your_range(20, 10))