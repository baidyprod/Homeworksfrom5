def your_all(iterable, /):
    for item in iterable:
        if bool(item) is False:
            return False
    return True