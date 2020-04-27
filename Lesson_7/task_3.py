# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.


import random

M = 5

orig_list = [random.randint(0, 100) for _ in range(2 * M + 1)]
print(f'дан массив: {orig_list}')
# print(sorted(orig_list), sorted(orig_list)[M])


count = [[0, 0] for i in range(len(orig_list))]
max_ = 0
for key_i, val_i in enumerate(orig_list):
    for val_j in orig_list:
        if val_j < val_i:
            count[key_i][0] += 1
        elif val_j > val_i:
            count[key_i][1] += 1

    if val_i > max_:
        max_ = val_i

res = 0
min_ = max_
for key, val in enumerate(count):
    med = abs(val[1] - val[0])
    if med < min_:
        min_ = med
        res = orig_list[key]
print(f'его медиана равна {res}')
