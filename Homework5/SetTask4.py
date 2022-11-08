set = {1, 2}
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}

res_a = set.intersection(set_a)
res_b = set.intersection(set_b)
res_c = set.intersection(set_c)

list = [res_a, res_b, res_c]

for item in list:
    if len(item) > 0:
        print("True")
    else:
        print("False")