# Работа по фотографии алгоритма в домашнем воркбуке

x = 10
y = 0
while x != 5:
    x = x - 1
    y = y + 2*y - 3
if x == y:
    x = x - y
    y = y + x
else:
    x = x + y
    y = y - x
print(y)


