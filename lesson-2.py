#---------------------------1--------------------------------#


my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4],
           (5, 6, 9.8), {7: 'seven', 8: 'eight'}, {9, 10},
           range(11), b'twelve', bytearray(b'thirteen'), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}){item} - {type(item)}")


#--------------------------2----------------------------------#


a_list = input("Цифры с пробелами - ").split()

for i in range(1, len(a_list), 2):
    a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]


print(a_list)

#-----------------------------3-------------------------------#

month = int(input("Введите порядковый номер месяца года: "))

month_list = ["Январь", "Февраль", "Март", "Апрель",
          "Май", "Июнь", "Июль", "Август",
          "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

month_numero = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
          5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
          9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

if month in month_numero:
    print(f"{month}-й месяй года - это {month_list[month - 1]}")
    print(f"{month}-й месяй года - это {month_numero[month]}")
else:
    print("Нет такого месяца")

#------------------------------------3a----------------------------------------#

while True:
    n_month = input("Введите номер месяца: ")
    if n_month.isdigit() and 0 < int(n_month) <= 12:
        season_name = ["зима", "весна", "лето", "осень", "зима"]
        print(f"{n_month} - это {season_name[int(n_month) // 3]}")
    else:
        print("Нет такого месяца")
    break

#----------------------------------------4------------------------------------#

string = input("Напишите несколько слов, отделяя их пробелами: ").split()

for i, word in enumerate(string, 1):
    print(f'{i}.{word[:10]}')

#---------------------------------------5-------------------------------------#

my_list = [17, 5, 3, 3, 2]

new_numb = int(input("Введите новое рейтинговое число (целое): "))
i = 0
for n in my_list:
    if new_numb <= n:
        i += 1
my_list.insert(i, int(new_numb))
print(my_list)

#-----------------------------------------6-----------------------------------#

goods = []
chars = {"название": "", "стоимость": "", "количество": "","ед. измерения": ""}
analyt = {"название": [], "стоимость": [], "количество": [],"ед. измерения": []}
numb = 0
while True:
    if input("Для выхода нажмите 'Q', для продолжения - 'Enter'").upper() == "Q":
        break
    numb +=1
    chars = chars.copy()
    for f in chars:
        pro = input(f'Введите свойство "{f}": ')
        chars[f] = int(pro) if f == "стоимость" or f == "количество" else pro
        analyt[f].append(chars[f])
        goods.append((numb, chars))
    print(f"{goods}")
    print(f'{"*" * 30}')
    for key, value in analyt.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)

#----------------------------------------------7----------------------------------#

