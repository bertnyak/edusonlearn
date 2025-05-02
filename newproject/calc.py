def calc_time (days, hours, minutes, seconds):
    return days * 86400 + hours * 3600 + minutes * 60 + seconds
inp = input('Введите временной промежуток в формате: число дней, число часов, число минут, число секунд ')
lst = inp.split(', ')
time = calc_time(int(lst[0]), int(lst[1]), int(lst[2]), int(lst[3]))
print('Введенный промежуток составляет', time, 'секунд.')
