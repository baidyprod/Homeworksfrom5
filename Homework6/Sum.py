def your_sum(iterable, /, start=0):
    res = 0
    res += start
    for item in iterable:
        res += item
    return res

print(sum(range(10)) == your_sum(range(10)))
print(sum([]) == your_sum([]))