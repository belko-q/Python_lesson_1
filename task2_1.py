a = input()
b = input()


try:
    a1 = float(a)
except ValueError:
    a1 = str(a)

try:
    b1 = float(b)
except ValueError:
    b1 = str(b)


type_a1 = type(a1)
type_b1 = type(b1)
if (type_a1 == float and type_b1 == float):
    if (a1 >= 3 and b1 >= 3 and a1 <= 21 and b1 <= 21):
        print(f'Сумма чисел: {a1+b1}')
    else:
        a1 = str(a1)
        b1 = str(b1)
        print(f'Строка: {a1 + b1}')
else:
    a1 = str(a1)
    b1 = str(b1)
    print(f'Строка: {a1 + b1}')


