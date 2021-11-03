#13.8.19
tor = int(input('Сколько билетов вы хотите приобрести? '))
count = 0
for i in range(1, tor+1):
    loki = int(input(f'Возраст {i} участника? '))
    if loki < 18:
        count += 0
    elif 18 <= loki < 25:
        count += 990
    else: count += 1390
if tor > 3:
    count *= 0.9
print(f'Общая стоимость: {round(count)} руб.')