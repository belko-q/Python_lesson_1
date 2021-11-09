import math

try:
    print('Введите первое число от 3 до 23: ')
    a = float(input())
    print('Введите второе число от 3 до 23: ')
    b = float(input())
    print('Введите знак (+,-,*,/): ')
    znak = input()

    if (a >= 3 and b >= 3 and a <= 23 and b <= 23):
        if znak in ('+', '-', '*', '/'):
            if znak == '+':
                print(a + b)
            elif znak == '-':
                print(math.fabs(a - b))
            elif znak == '*':
                print(a * b)
            elif znak == '/':
                if b != 0:
                    print(a / b)
                else:
                    print("Деление на ноль.")
        else:
            print("Неверный знак операции.")
    else:
        print("Введены числа вне диапазона.")


except ValueError:
    print('Введен некорректый символ.')
