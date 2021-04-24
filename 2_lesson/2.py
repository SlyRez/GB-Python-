my_list = []
count_el = int(input('Количество элементов в листе: '))
n = 0
while n < count_el:
    my_list.append(input('Укажите элемент списка '))
    n = n + 1
print(my_list)
my_list_el = count_el - count_el % 2 # тут решил окрглить до четного числа, что бы не трогать последний элемент
i = 0
el_1 = None
el_2 = None
while i < my_list_el:
    el_1 = my_list[i]
    el_2 = my_list[i+1]
    my_list[i] = el_2
    my_list[i+1] = el_1
    i = i + 2
    print(my_list)