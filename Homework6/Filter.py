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