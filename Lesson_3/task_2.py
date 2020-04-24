# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.


import random

SIZE = 10
source = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]

print(f'В массиве {source}')
even = [id for id, val in enumerate(source) if val % 2 == 0]
print(f'четные числа имеют следующие индексы: {even}')
