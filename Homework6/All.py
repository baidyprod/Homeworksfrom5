def your_all(iterable, /):
    for item in iterable:
        if bool(item) is False:
            return False
    return True


print(all([]) == your_all([]))
print(all([True, False]) == your_all([True, False]))
print(all([True, True]) == your_all([True, True]))
print(all([False, False]) == your_all([False, False]))
