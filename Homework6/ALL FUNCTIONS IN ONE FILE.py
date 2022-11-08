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
    res = []  #Result list
    list_not_final = []  #List which will be fullfilled with n-indexed elements from each iterable
    b = [*iterables]  #Variable b is a list of different iterables of different types
    a = tuple([list(word) for word in b])  #Variable "a" becomes a tuple of iterables converted to lists
    e = tuple([list(word) for word in b])  #Variable "e" is the same as "a" but has different id (e = a[:] and e = a.copy() don't work idk why :/)
    for item in e:  #Next three lines convert each digit in "e" list of list to a string. We need to do this because function min (3 lines lower) doesn't work without this.
        for digit in item:
            item[item.index(digit)] = str(digit)
    list_of_length = []  #Next 4 lines we need to count the shortest iterable which was input
    for item in e:
        list_of_length.append(len(item))
    minimum = min(list_of_length)
    for i in range(minimum):  #"i" takes the index of item in iterable
        for o in range(len(a)):  #"o" takes the index of iterable
            list_not_final.append((a[o][i]))  #List_not_final is being appended by items of same index in different iterables
        res.append(tuple(list_not_final))  #Result list is being appended by the previous list, converted into tuple
        list_not_final = []  #List_not_final is being cleared before the next repeat of main loop
    return res  #After all iterations our function returns the result list



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
    if function == None:
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