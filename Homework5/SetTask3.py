set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}

res_a_b = set_a.intersection(set_b)
res_b_c = set_b.intersection(set_c)
res_a_c = set_a.intersection(set_c)

print('res_a_b = ', res_a_b)
print('res_b_c = ', res_b_c)
print('res_a_c = ', res_a_c)