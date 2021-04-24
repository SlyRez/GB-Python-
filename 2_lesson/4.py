my_string = str(input('введите несколько слов: '))
my_word = my_string.split()
n = 1
for i in my_word:
    if len(i) > 10:
        print(n, ' ', i[0:10])
        n = n + 1
    else:
        print(n, ' ', i)
        n = n +1