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

print(list(map(int, '1234567890')) == your_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == your_map(min, range(10), range(20, 30), range(25, 15, -1)))