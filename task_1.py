# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

number = int(input('Введите натуральное число обозначающее максимальную степень многочлена (от 0 до 100): '))

def polynomial(k) -> str:
    my_polynomial = []
    while k >= 0:
        a = randint(0, 100)
        if a == 0:
            k -= 1
        elif a == 1 and k > 1:
            my_polynomial.append(f'x**{str(k)}')
            k -= 1
        elif a == 1 and k == 1:
            my_polynomial.append('x')
            k -= 1
        elif a == 1 and k == 0:
            my_polynomial.append('1')
            k -= 1
        elif k == 1:
            my_polynomial.append(f'{str(a)}*x')
            k -= 1
        elif k == 0:
            my_polynomial.append(f'{str(a)}')
            k -= 1
        else:
            my_polynomial.append(f'{str(a)}*x**{str(k)}')
            k -= 1
    return ' + '.join(my_polynomial) + ' = 0'

new_polynomial = polynomial(number)

print(new_polynomial)

# def write_to_file(file, polynomial):
#     data = open(file, 'a')
#     data.writelines(polynomial)
#     data.close()
#     exit()

# write_to_file('file_1.txt', new_polynomial)
# write_to_file('file_2.txt', new_polynomial)
