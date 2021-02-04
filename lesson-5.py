#-------------------------------1---------------------------#

a_file = open('python_text.txt', 'w', encoding='utf-8')

line = " "
while line:
    line = input("Input new phrase or space to stop: ")
    a_file.write(f"{line}\n") if line != "" else a_file.close()

#-----------------------2------------------------------------#

with open("py_text-2.txt", encoding="utf-8") as b:
    b_line = b.readlines()
    for index, value in enumerate(b_line, 1):
        n_words = len(value.split())
        print(f"Строка {index} содержит {n_words} слов")

#----------------------3---------------------------------------#

with open ("py_salaries.txt", 'r', encoding='utf-8') as c:
    empl_list = {line.split()[0]: float(line.split()[1]) for line in c}
    print(f"Средняя ЗП = {round(sum(empl_list.values()) / len(empl_list), 2)}\n"
          f"Сотрудники низкооплачиваемые {[d[0] for d in empl_list.items() if d[1] < 20000]}")

#----------------------4-----------------------------------#

ru_eng_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("py_eng_numb.txt", 'w', encoding='utf-8') as eng_file:
    with open("py_rus_numb.txt", encoding='utf-8') as ru_file:
        eng_file.writelines([line.replace(line.split()[0], ru_eng_dict.get(line.split()[0])) for line in ru_file])


#------------------------5-----------------------------#

from random import randint

with open("sum_of_numbers.txt", mode='w+', encoding='utf-8') as ab_file:
    ab_file.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    ab_file.seek(0)
    print(sum(map(int, ab_file.readline().split())))

#--------------------------6---------------------------#

arr = {}
with open('text_excersises.txt', 'r', encoding='utf-8') as c_file:
    for line in c_file:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        arr[line.split()[0]] = sum(map(int, line.split()[1:]))
    print(f"Общее количество часов по предмету: \n{arr}")

#-------------------------7-------------------------------#

import json
with open("exc7.json", 'w', encoding='utf-8') as a_script:
    with open("7.txt", encoding="utf-8") as a_ob:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in a_ob}
        numb = [profit, {"средний заработок": round(sum([int(i) for i in profit.values() if int(i) > 0] /
                                                        len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(numb, a_script, ensure_ascii=False, indent=4)

