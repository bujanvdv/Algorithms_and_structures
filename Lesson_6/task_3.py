# 3 варианта одной задачи

# Python 3.8.0
# OS Windows 10 - 64bit

from count_size import count_size


n = int(input('Введите n: '))


def var_sum(var_lst):
    summa = 0
    for i in var_lst:
        summa += count_size(i)
    print(f'Под переменные задействованно {summa} байт памяти')


sum_ = 0
for i in range(n):
    sum_ += (-1) ** i / 2 ** i

var_sum([sum_, i])
# Под переменные задействованно 30 байт памяти

item = 1
summ = 0
for j in range(n):
    summ += item
    item /= -2

var_sum([item, summ, j])

# Под переменные задействованно 46 байт памяти

summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))

var_sum([summa_2])
# Под переменные задействованно 16 байт памяти

# Очевидно, что по памяти эффективнее программа с одной переменной
