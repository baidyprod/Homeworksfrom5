def your_any(iterable, /):
    for item in iterable:
        if bool(item) is True:
            return True
    return False

print(any([]) == your_any([]))
print(any([True, False]) == your_any([True, False]))
print(any([True, True]) == your_any([True, True]))
print(any([False, False]) == your_any([False, False]))