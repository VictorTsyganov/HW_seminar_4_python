# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(file):
    data = open(file, 'r')
    for line in data:
        polynomial = line
    data.close()
    return polynomial
    
polynomial_1 = read_file('file_1.txt')
polynomial_2 = read_file('file_2.txt')

def ind_polynomial(my_polynomial):
    new_polynomial = (my_polynomial.replace(' ', '').replace('=0', '')
                      .replace('+', ' ').replace('-', ' -'))
    new_polynomial = new_polynomial.split()
    for i in range(len(new_polynomial)):
        if new_polynomial[i].startswith('x'):
            temp = new_polynomial[i].replace('x', '1*x')
            new_polynomial[i] = temp
        elif new_polynomial[i].startswith('-x'):
            temp = new_polynomial[i].replace('x', '-1*x')
            new_polynomial[i] = temp
        elif new_polynomial[i].endswith('x'):
            temp = new_polynomial[i].replace('x', 'x**1')
            new_polynomial[i] = temp
        elif new_polynomial[i].isdigit():
            temp = new_polynomial[i] + '*x**0'
            new_polynomial[i] = temp
    new_dict = {}        
    for item in new_polynomial:
        new_dict[int(item.split('*x**')[1])] = int(item.split('*x**')[0])
    return new_dict

dict_1  = ind_polynomial(polynomial_1)
dict_2  = ind_polynomial(polynomial_2)

sum_dict = {}

if len(dict_1) > len(dict_2):
    for key in dict_1:
        if key in dict_2.keys():
            sum_dict[key] = dict_1[key] + dict_2[key]
        else:
            sum_dict[key] = dict_1[key]
else:
    for key in dict_2:
        if key in dict_1.keys():
            sum_dict[key] = dict_1[key] + dict_2[key]
        else:
            sum_dict[key] = dict_2[key]    

print(sum_dict)

def polynomial(my_dict) -> str:
    my_polynomial = []
    for key,value in my_dict.items():
        if value == 0:
            pass
        elif value == 1 and key > 1:
            my_polynomial.append(f'x**{str(key)}')
        elif value == 1 and key == 1:
            my_polynomial.append('x')
        elif value == 1 and key == 0:
            my_polynomial.append('1')
        elif key == 1:
            my_polynomial.append(f'{str(value)}*x')
        elif key == 0:
            my_polynomial.append(f'{str(value)}')
        else:
            my_polynomial.append(f'{str(value)}*x**{str(key)}')
    return ' + '.join(my_polynomial) + ' = 0'

sum_polynomial = polynomial(sum_dict)
print(sum_polynomial)

def write_to_file(file, polynomial):
    data = open(file, 'a')
    data.writelines(polynomial)
    data.write('\n')
    data.close()
    exit()

write_to_file('file_sum.txt', sum_polynomial)
