from pprint import pprint

dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}

res1 = dict_a | dict_b

res = dict()

set1 = set()
for i in range(0,11,2):
    set1.add(str(i))

for item in res1:
    check = set1.intersection(set(item))
    if len(check) > 0:
        continue
    res.update({item: res1.get(item)})

pprint(res)