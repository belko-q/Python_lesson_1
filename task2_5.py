a = input()
to_list = list(a)
summa = 0

try:
    for i in to_list:
        summa = summa + int(i)
    print(summa)

except ValueError:
    print("Введен некорректный символ.")
