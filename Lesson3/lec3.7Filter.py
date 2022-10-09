# Функция filter применяет указанную функцию к каждому элементу итерируемого объекта и возвращает
# итератор с теми объектами, для которых функция вернула True
# f(x) => x - четное
# map (f, [ 1,  2,  3,  4,  5 ])
#               ↓       ↓
#             [ 2       4  ]

# нельзя пройтись дважды
#  как и с map у filter первый аргумент ф-я, второй - данные
data = [x for x in range(10)]
res = filter(lambda x: x % 2 == 0, data)
print(res)                           # вывод: <filter object at 0x000001E6F15B3DC0>

res = list(filter(lambda x: not x % 2, data))
print(res)                           # вывод: [0, 2, 4, 6, 8]