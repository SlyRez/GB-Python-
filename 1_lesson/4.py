# эта задача для меня была сложной, очень долго сидел искал какие то пути и решения но безуспешно
# код ниже собирал из гугла, гдето вроде понял почему и как нужно писать,
# какие то строки "подбором" прописывал и не понял как заработало
# в общем, сам бы точно не решил ее, можно ли получить советы по этой тематике или разобрать ее на уроке?
# хотя бы просто логику, по которой идти при написании кода
# может быть она и простая, но вот мой мозг отказывается осознать.
# Даже с нуля не смогу наверное снова повторить без гугла, как такое можно с нуля написать =(

n = abs(int(input()))  # указываем что  нам нужны положительные и целые числа
max = n % 10 # кладем в переменную последнюю цифру от введенного числа, будем сравнивать дальше с ней
print(n)
print(max)
while n >= 1:  # проверка оставшегося числа, если вдруг уже ушли в десятичные то прекращаем цикл?
    print(n)
    n = n // 10  # отрезали последнюю цифру от числа и перезаписали
    print(n)
    if n % 10 > max: # берем следующую последнюю цифру и сравниваем с той что уже в max
        max = n % 10
        print(max)
    if n > 9: # продолжаем пока наше введенное число не станет 1-но значным
        continue
    else:
        print("Ответ ", max)
        break
