# Множества - Set - Неупорядоченные коллекции данных, содержащие неповторяющиеся элементы.
# Во множестве не м.б. двух одинаковых элементов.
colors = {'Red', 'Green', 'Blue'}
print(type(colors))   # <class 'set'>
colors.add('Red')
print(colors)         # {'Red', 'Blue', 'Green'} - не добавить такой же элемент
colors.add('Gray')
print(colors)         # {'Green', 'Red', 'Gray', 'Blue'} - добавили
colors.remove('Red')
print(colors)         # {'Blue', 'Gray', 'Green'} - удалили
#colors.remove('Red')
#print(colors)         # KeyError: 'Red' - нет элемента для удаления
colors.discard('Red')  # этот метод, при удалении элемента, которого нет во множестве, не возвращает ошибку.
print(colors)
colors.clear()         # иозвращает пустое множество set()
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()           # вывод: {1, 2, 3, 5, 8} - копия
print(c)
u = a.union(b)         # вывод: {1, 2, 3, 5, 8, 13, 21} - объединение
print(u)
i = a.intersection(b)  # вывод:  {8, 2, 5} - пересечение
print(i)
dl = a.difference(b)   # вывод:{1, 3} - разница
print(dl)
dr = b.difference(a)   # вывод:{13, 21} - разница
print(dr)
q = a.union(b).difference(a.intersection(b))
print(q)               # вывод: {1, 21, 3, 13} - 'элементы множеств a и b, которые не пересекаются
# По мимо изменяеьых множеств, множества мюбю неизменяемые:
s = frozenset(a) # вывод: {1, 2, 3, 5, 8} - неизменяемое замороженное множество
print(a)
