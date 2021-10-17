
second_now = int(input())

if second_now > 0 and second_now <= 86400:
    seconds = second_now % 60
    munutes_with_hours = second_now - seconds
    #print(munutes_with_hours)
    if munutes_with_hours >= 3600:
        minutes = (munutes_with_hours // 60) % 60
        hours = (munutes_with_hours - minutes) // 3600
    else:
        minutes = munutes_with_hours // 60
        hours = 0
    print(f'{hours} {minutes} {seconds}')
else:
    print('Введено неверное значение.')
