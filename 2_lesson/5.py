'''
# одна из первых попыток
my_list = [7, 5, 3, 3, 2]
new_count = int(input('Введите оценку (до 10): '))
if 0 < new_count <= 10: # проверка, введный рейтинг 0-10
    for i in my_list:
        if i <= new_count:
            my_list.insert(my_list.index(i), new_count)
            print('текущий рейтинг: ', my_list)
            break
        elif i >= new_count >= i - 1:
            my_list.insert(my_list.index(i) + 1, new_count)
            print('текущий рейтинг: ', my_list)
            break
        elif i < new_count:
            my_list.append(new_count)
            print(my_list)
            break
        else:
            continue
else:
    print("Не корректная оценка")
'''

'''
# новые попытки
my_list = [7, 5, 3, 3, 2]
new_count = int(input('Введите оценку (до 10): '))
if 0 < new_count <= 10: # проверка, введный рейтинг 0-10
    for i in my_list:
        if new_count >= i:
            my_list.insert(my_list.index(i), new_count)
            print(my_list)
            break
        else:

else:
    print("Не корректная оценка")
'''

'''
# простая сортировка значений
my_list = [7, 5, 3, 3, 2]
new_count = int(input('Введите оценку (до 10): '))
if 0 < new_count <= 10: # проверка, введный рейтинг 0-10
    my_list.append(int(new_count))
    my_list.sort(reverse=True)
    print(my_list)
else:
    print("Не корректная оценка")
'''