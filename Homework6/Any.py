def your_any(iterable, /):
    for item in iterable:
        if bool(item) is True:
            return True
    return False