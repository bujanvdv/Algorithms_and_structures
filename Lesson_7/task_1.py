# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.



import random
import timeit


def bubble_sort(orig_list):

    n = len(orig_list)

    while n > 0:
        for i in range(1, n):
            if orig_list[-i] > orig_list[-(i + 1)]:
                orig_list[-i], orig_list[-(i + 1)] = orig_list[-(i + 1)], orig_list[-i]

        n -= 1
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(f'source: {orig_list}')
print(f'sorted: {bubble_sort(orig_list[:])}')


print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=100))
