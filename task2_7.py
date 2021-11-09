a = float(input())
years = int(input())

year_koef = 1.1

for i in range(1, years+1):
    a = round((a * year_koef), 2)

print(f"Через {years} лет сумма будет {a}.")
