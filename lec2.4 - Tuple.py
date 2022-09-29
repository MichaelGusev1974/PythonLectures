# Кортеж - Tuple - неизменяемый "список"
t = ()
print(type(t))                        # <class 'tuple'>

t = (1,)
print(type(t))                        # <class 'tuple'>

t = (1)                               # <class 'int'>
print(type(t))

t = (26, 6, 1974)                     # <class 'tuple'>
print(type(t))

colors = ['Red', 'Green', 'Blue']
print(colors)                         # ['Red', 'Green', 'Blue']
t = tuple(colors)
print(t)                              # ('Red', 'Green', 'Blue')

a = (2, 3, 4, 25, 36)
print(a)
print(a[0])
print(a[-1])
print(a[-2])
for i in a:
    print(i, end=' ')

print()
# Можно распаковать кортеж в отдельные переменные
n = tuple(['white', 'Black', 'Gray'])  # двойное преобразование: создаем список, далее конвертируем в кортеж
white, Black, Gray = n                 # здесь распаковываем и превращаем в три независимые переменные
print('w: {} b: {} g: {}'.format(white, Black, Gray))