def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split() # split() делит строку на строки: ['1', '2', '3', '5', '8', '15', '23', '38']
print(data)

res = select(int, data)             # наша ф-я select, с аргументами: ф-я int для преобразования списка строк в список чисел и сам список data
print(res)                          # вывод: [1, 2, 3, 5, 8, 15, 23, 38]
res = where(lambda x: not x%2, res) # 1-й аргумент lambda-ф-я, кот. проверяет четность, второй наш int res
print(res)                          # вывод: [2, 8, 38]
res = select(lambda x:(x, x**2),res)# 1-й аргумент lambda-ф-я, кот.формирует кортеж из пар чисел(четное, оно же во 2 степени), второй наш int четный res
print(res)                          # вывод: [(2, 4), (8, 64), (38, 1444)]

