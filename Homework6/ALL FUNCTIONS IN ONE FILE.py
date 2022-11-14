def your_any(iterable, /):
    for item in iterable:
        if bool(item) is True:
            return True
    return False



def your_all(iterable, /):
    for item in iterable:
        if bool(item) is False:
            return False
    return True



def your_zip(*iterables):
    tmp = []
    for coll in iterables:
        tmp.append(len(coll))
    min_count_el_in_coll = min(tmp)
    res = []
    for index in range(min_count_el_in_coll):
        tmp = []
        for coll in iterables:
            tmp.append(coll[index])
        res.append(tuple(tmp))
    return res



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


def your_sum(iterable, /, start=0):
    res = 0
    res += start
    for item in iterable:
        res += item
    return res



def your_enumerate(iterable, start=0):
    indexes = list(range(start, start+len(iterable)))
    res = list(zip(indexes, iterable))
    return res



def your_filter(function, iterable):
    res = []
    if function is None:
        for item in iterable:
            if bool(item):
                res.append(item)
    else:
        for item in iterable:
            if bool(function(item)):
                res.append(item)
    return res



def your_map(func, *iterables__) -> list:
    '''
    Make a list that computes the function using arguments from each of the iterables.
    Stops when the shortest iterable is exhausted.
    '''
    res = []
    iterables = [*iterables__]
    iterables_edited = [list(item) for item in iterables]
    if len(iterables) == 1:  #If iterable is only 1, the function works with it's units
        for item in iterables_edited:
            for unit in item:
                a = func(unit)
                res.append(a)
    else:  #If there are more than 1 iterable, the function works with iterables
        a = func(iterables_edited)
        for item in a:
            res.append(item)
    return res