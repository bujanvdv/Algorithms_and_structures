# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.


n = input("Введите знак операции: +, -, *, /. Для завершения введите 0: ")

while n != '0':
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    if n in ('+', '-', '*', '/'):
        if n == '+':
            print(f'Результат сложения {a} + {b} = ', (a + b))
        elif n == '-':
            print(f'Результат вычитания {b} - {a} = ', (a - b))
        elif n == '*':
            print(f'Результат умножения {a} * {b} = ', (a * b))
        elif n == '/':
            if b != 0:
                print(f'Результат деления {a} / {b} = ', (a / b))
            else:
                print("Делить на ноль нельзя!")
    else:
        print("Введен не верный символ. Используйте:+, -, *, /, 0")
    n = input("Введите знак операции: +, -, *, /. Для завершения введите 0: ")
