def your_range(a:int, b:int=None, c:int=None) -> list:
    '''
    Returns a list of integers in such way:
    range(stop) - default start value = 0, default step value = 1
    range(start, stop) - default step value = 1
    range(start, stop, step)
    '''
    if b == None and c == None:
        start = 0
        stop = a
        step = 1
    elif c == None:
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