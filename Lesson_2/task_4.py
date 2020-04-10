# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


n = int(input("Введите длинну ряда чисел 1 -0.5 0.25 -0.125 ...: "))
summ = 0   # сумма элементов последовательности
m = 1      # значение элемента последовательности

for i in range(n):
    summ += m
    m /= -2

print(f'Сумма элементов последовательности длинной {n} равна: {summ}')
