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

print(list(zip(range(10), range(15), range(8))) == your_zip(range(10), range(15), range(8)))
print(list(zip(range(10), range(15), [])) == your_zip(range(10), range(15), []))
print(list(zip(range(10))) == your_zip(range(10)))