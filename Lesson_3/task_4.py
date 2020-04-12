# Определить, какое число в массиве встречается чаще всего.


import random

SIZE = 100
source = [random.randint(0, SIZE) for _ in range(0, SIZE)]

count_dict = {}
for val in source:
    count = 0
    for i in source:
        if i == val:
            count += 1
    count_dict[count] = val

max_ = 0
for j in count_dict:
    if j > max_:
        max_ = j

print(f'в массиве: {source}')
print(f'часто всиречаемое число: {count_dict[max_]} (повторов: {max_})')
