#-----------------------------1-------------------------#

def div(x_1, x_2):
    try:
        x_1, x_2 = int(x_1), int(x_2)
        div_num = x_1 / x_2
    except ValueError:
        return "Ошибка!"
    except ZeroDivisionError:
        return "Деление на 0 невозможно!"
    return round(div_num, 2)


print(div(input("Введите первое число - "), input("Введите второе число - ")))

#-------------------------------------2--------------------------#

def pers_data(**kwargs):
    return " ".join(kwargs.values())


print(pers_data(name=input("Ваше имя: "), surname=input("Ваша фамилия: "),
                bday=input("Дата рождения: "), city=input("Город проживания: "),
                email=input("Ваша эл.почта: "), phone=input("Ваш номер телефона: ")))

#------------------------------------3---------------------------#

def x_func(n_1, n_2, n_3):
    x_list = [n_1, n_2, n_3]
    try:
        x_list.remove(min(x_list))
        return sum(x_list)
    except TypeError:
        return "Вводите только числа!"

print(x_func(float(input("Первое число - ")), float(input("Второе число - ")), float(input("Третье число - "))))

#-----------------------------------4---------------------------#

def a_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Неверно введены числа"
        else:
            res = 1
            for _ in range(abs(y)):
                res /= x
            return f'Результат возведения х в степень у: {round(res, 5)}'
    except ValueError:
        return "Вводите только числа!"

numb1 = input("Введите положительное число, х = ")
numb2 = input("Введите отрицательное целое число, y = ")

print(a_func(numb1, numb2))

#---------------------------------------5----------------------------------#

def sum_num():
    s = 0
    while True:
        b_list = input("Введите число или x для выхода").split()
        for num in b_list:
            if num == "x":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Для завершения работы - нажмите x.")
            print(f'Сумма чисел равна = {s}')


print(sum_num())

#-----------------------------------------6------------------------------#

def c_func():
    for word in input("Введите слова строчными буквами с пробелами: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - только малыми буквами")

    c_func()
