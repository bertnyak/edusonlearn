'''
Напишите программу: запросите у пользователя целое число и выведите на экран информацию о том, четное оно или нечетное.'''

a = int(input("Введите чилсо, чтобы узнать четное оно либо нет: "))

if a%2 == 0:
    print("Четное")
else:
    print("Нечетное")

print(a)