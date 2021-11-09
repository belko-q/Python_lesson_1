import math

print('Введите номер, соответствующий фигуре, для которой будет рассчитана площадь:\n 1 - прямоугольник\n 2 - треугольник\n 3 - круг ')

def rectangle_square(x, y):
    S = x * y
    return S

def triangle_square(a, b, c):
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S

def circle_square(r):
    S = math.pi * math.pow(r, 2)
    return S

try:
    figure_type = int(input())

    if figure_type == 1:
        print('Введите длины двух сторон:')
        x = float(input())
        y = float(input())
        S = rectangle_square(x, y)
        print(f'Площадь прямоугольника равна {S}.')
    elif figure_type == 2:
        print('Введите длины трех сторон:')
        a = float(input())
        b = float(input())
        c = float(input())
        S = triangle_square(a, b, c)
        print(f'Площадь треугольника равна {S}.')
    elif figure_type == 3:
        print('Введите радиус:')
        r = float(input())
        S = circle_square(r)
        print(f'Площадь круга равна {S}.')
    else:
        print('Введен некорректый номер.')

except ValueError:
    print('Введен некорректый символ.')

