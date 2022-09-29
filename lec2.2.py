def new_string(simbol, count):
    return simbol * count
print(new_string('!', 20))
# если укажем один параметр print(new_string('!'))- будет error
# ошибки не будет, если в функции второму параметру явно присвоить значение:
def new_string2(simbol, count = 3):
    return simbol * count
print(new_string('!', 11))
print(new_string2('!'))
# Python распознает тип данных в момент вызова функции, если в ка-ве аргумента передадим число, возврат число
print(new_string(4, 12))

def concatinatio(*params):
    res:  str = ""               # НЕ Обязательно!!! здесь мы  при объявлении переменной res явно объявляем тип данных
    for i in params:             # для работы с числами тип str нужно поменять на int
        res += i
    return res

print(concatinatio('a', 'b', 'c', 'd'))
print(concatinatio('a', '1', 'c', '2'))
#print(concatinatio('1', '2', '3', '2')) # для работы с числами в функции concatinatio тип str нужно поменять на тип int

def concatinatio1(*params):
    res:  int = 0               #  НЕ Обязательно!!! здесь мы  при объявлении переменной res явно объявляем тип данных
    for i in params:
        res += i
    return res
print(concatinatio1(1, 2, 3, 4))
