# Получение коэффициенов
first_cofficient = int(input('a = ', ))  
second_cofficient = int(input('b = ', ))   
third_cofficient = int(input('c = ', ))    

# Решение по сокращенной формуле, т.к. b - четное
if first_cofficient!= 0 and second_cofficient % 2 == 0 and third_cofficient!= 0:  
    k = second_cofficient / 2
    d1 = k ** 2 - first_cofficient * third_cofficient
    k1 = (-k + d1 ** 0.5) / first_cofficient
    k2 = (-k - d1 ** 0.5) / first_cofficient

    print('так как второй кофициент - четное число, решаем по сокращенной формуле')
    print(f'k1 = {k1}')
    print(f'k2 = {k2}')  

# Решение уравнения при с = 0
if first_cofficient!= 0 and third_cofficient== 0 and second_cofficient!= 0:     
    print(f'корень уравнения равен либо нулю, либо {-second_cofficient / first_cofficient}')

# решение уравнения при b = 0 и c = 0 
if first_cofficient != 0 and second_cofficient== 0 and c == 0:
    print(f'корни уравнения равны нулю, peremennaya1 * x ** 2 = 0')

# Решение полного уравнения
if first_cofficient!= 0 and second_cofficient % 2 != 0 and third_cofficient!= 0:
    d = second_cofficient ** 2 - 4 * first_cofficient * third_cofficient
    if d > 0:
        k1 = (-second_cofficient + d ** 0.5) / (2 * first_cofficient)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(k1, 2)}')
        k2 = (-second_cofficient - d ** 0.5) / (2 * first_cofficient)
        print(f'второй корень равен: {round(k2, 2)}')  
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет') 
    else:
        k = -second_cofficient / (2 * first_cofficient)
        print(f'уравнение имеет один корень: {k}')

# решение уравнения при b = 0
        if first_cofficient != 0 and c != 0 and second_cofficient == 0:
            if (-third_cofficient / first_cofficient) >= 0:
                k1 = (-third_cofficient / first_cofficient) ** 0.5
                print(f'первый корень равен: {k1}')
                k2 = (-1) * ((-third_cofficient / first_cofficient) ** 0.5)
                print(f'второй корень равен: {k2}')
        if ( - third_cofficient / first_cofficient ) < 0:
            print(
                f' -c / peremennaya1 = : {-c / peremennaya1}, '
                f'т.е. < 0, поэтому действительных корней нет')

# решение уравнения при b = 0 и c = 0
if first_cofficient != 0 and second_cofficient == 0 and third_cofficient == 0:     
    print(f'корни уравнения равны нулю, peremennaya1 * x ** 2 = 0')