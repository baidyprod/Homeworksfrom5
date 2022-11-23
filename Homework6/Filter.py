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

print(list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == your_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
print(list(filter(lambda a: a % 2 == 0, range(10+1))) == your_filter(lambda a: a % 2 == 0, range(10+1)))