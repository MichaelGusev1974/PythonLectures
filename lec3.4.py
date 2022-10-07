# В файле хранятся числа. Нужно выбрать четные и составить список пар (число; квадрат числа)
# пример: [1 2 3 5 8 15 23 38] вывод: [(2,4), (8,16)]

with open('task.txt', 'w+') as task:
    task.write('1 2 3 5 8 15 23 38')

# with open('task.txt', 'r') as task:
#     # print(task.readable())               # вывод: True
#     data = task.read()
#     print(task.read())
#
# data = map(int, data.split(' '))   # map - ф-я выполняемая
# data = list(data)
# print(data)
#
# f = lambda a, b: a**b
# # List Comprehencion - быстрое создание списков
# # [выражение для каждого значения из последовательности]
# print([i + i for i in data])
# print([(i, f(i, 2)) for i in data]) # передали ф-ю f = lambda a, b: a**b
path = 'C:/Users/Михаил/Desktop/Обучение в GeekBrains/Python/PythonLectures/task.txt' # путь к файлу
f = open(path, 'r')                   # связываем файловую переменную f с нашим файлом на диске
data = f.read() + ' '                 # считываем всё, что есть в строке и искусственно добавляем пробел
f.close()                             # закрываем файл

numbers = []                          # пустой список для дальнейшего заполнения
while data != '':                    # проверка в цикле: пока строка НЕ пустая
    space_pos = data.index(' ')       # найти первую позицию пробела
    numbers.append(int(data[:space_pos]))  # от первого символа до первой позиции пробела, превпатить в число, добавить в список numbers
    data = data[space_pos + 1:]       # обновить строку

out = []                              # новый список
for e in numbers:                     # перебор значений элементов
    if not e % 2:                     # проверка условия, что число четное
        out.append((e, e**2))         # формируем кортеж из четных эл-ов и их значерий во 2 степени
print(out)






