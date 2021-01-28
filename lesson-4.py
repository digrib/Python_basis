#----------------------------1----------------------#

from sys import argv

def sal():
    try:
        t, r, b = map(float, argv[1:])
        print(f"Зп = {t * r + b}")
    except ValueError:
        print("Введите 3 числа. Без пробело и не строкой!")

sal()

#--------------------------------2-------------------------

a_list = [30, 2, 1, 4, 1, 1, 4, 10, 7, 1, 78, 12, 55]
big_val = [a_list[numb] for numb in range(1, len(a_list)) if a_list[numb] > a_list[numb - 1]]
print(big_val)#

import random

b_list = [random.randint(0, 1000) for i in list(range(0, random.randint(2, 20)))]
answ_l = [i for numb, i in enumerate(b_list[1:]) if i > b_list[numb]]

print(b_list)
print(answ_l)

#------------------------------------------------------3----------------------------#

c_list = [a for a in range(20, 241) if a % 20 == 0 or a % 21 == 0]
print(c_list)

#-----------------------------------------4-----------------------------#

from random import randint

d_list = [randint(-10, 10) for _ in range(20)]
e_list = [b for b in d_list if d_list.count(b) == 1]
print(f"{d_list}")
print(f"{e_list}")

#---------------------5-------------------------------------#

from functools import reduce

def f_list(f_1, f_2):
    return f_1 * f_2

g_list = [g for g in range(100, 1001, 2)]
print(f"{g_list}")
print(f"{reduce(f_list, g_list)}")

#-----------------------------6-------------------------------#

from itertools import count, cycle

a_count = count(int(input("Введите число: ")))
a_cycle = cycle(input("введите слово: "))

for _ in range(5):
    print("(count, cycle) = ({},{})".format(next(a_count), next(a_cycle)))
