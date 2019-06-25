import typing

__author__ = 'Menkov F.A.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print("Задача-1")
print("")
num_strings = '58375'
print('Решение через max(num_1) = ', max(num_strings))

num_list = []
for num_string in num_strings:
    num_int = int(num_string)
    num_list.append(num_int)

print('Решение через цикл for: ',max(num_list))


# for num in y:


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
print("Задача-2")
print("")
num_1 = input('Введите число 1: ')
num_2 = input('Введите число 2: ')
print(f'num_1 = {num_1}, num_2 = {num_2}')
print("ВЖУХ!")
num_2, num_1 = num_1, num_2
print("теперь число 2 = ", num_2, "раньше оно было число 1")
print("теперь число 1 = ", num_1, "раньше оно было число 2")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Задача-3")
print("")
import math

print('ax^2+bx+c=0')
a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
D = (b^2)-(4*a*c) # дискриминант
if D > 0:
    x1 = ((-b)-math.sqrt(D))/(2*a)
    x2 = ((-b)+math.sqrt(D))/(2*a)
    print(f'X1 = {x1}')
    print(f'X2 = {x2}')
elif D == 0:
    x1 = (-b)/(2*a)
    print(f'Уравнение имеет один корень X = {x1}')
elif D < 0:
    print('Корней нет')
