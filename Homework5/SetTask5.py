set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}

res = set_a.union(set_b, set_c)
res1 = set()
res2 = set()

for item in res:
    if item % 2 == 0:
        res1.add(item)
    else:
        res2.add(item)

print(res1)
print(res2)