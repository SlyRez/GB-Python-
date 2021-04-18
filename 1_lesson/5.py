profit = int(input('Введите выручку фирмы '))
costs = int(input('Введите издержки фирмы '))
if profit > costs:
    print('Есть прибыль! Рентабельность: ', profit / costs)
    workers = int(input('Сколько сотрудников в фирме?'))
    print('Прибыль на одного сотрудника: ', profit / workers)
elif profit < costs:
    print('Фирма в убытке!')
elif profit == costs:
    print('Вышли на себестоимость!')