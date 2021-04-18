inp_sec = int(input())
s = inp_sec % 60
m = (inp_sec // 60) % 60
h = inp_sec // 3600
print(s)
print(m)
print(h)
if s < 10:
    s = '0' + str(s)
if m < 10:
    m = '0' + str(m)
if h < 10:
    h = '0' + str(h)
print(h, ':', m, ':', s)
