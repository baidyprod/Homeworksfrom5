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