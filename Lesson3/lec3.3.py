# List Comprehencion
# [exp for item in iterable]
# [exp for item in iterable(in conditional)]
# [exp <in conditional> for item in iterable(in conditional)]

# 1. [exp for item in iterable]
# list = []
# for i in range(0, 21):
#     #if i % 2 == 0:
#         list.append(i)
#
# print(list)
list = []
list = [i for i in range(1, 21)] # более короткаяя запись заполнения списка, функционально то же, что и описано выше.
print(list) # вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Так же можно прописывать условие:
list1 = []
list1 = [i for  i in range(1, 21) if i % 2 == 0]
print(list1) # вывод: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# список кортежей:
list2 = []
list2 = [(i, i) for  i in range(1, 21) if i % 2 == 0]  # добавили (i, i)
print(list2) # вывод: [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]
# Список например возведения числа в 3 степень:
def f(x):
    return x**3

list3 = []
list3 = [f(i) for i in range(1, 21) if i % 2 == 0] # выборка - список четных чисел от 1 до 20, ф-я f числа из выборки-списка возводит в 3 степень.
print(list3) # вывод: [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]
# Список например возведения числа в 3 степень, для наглядности в кортеже:
list4 = []
list4 = [(i, f(i)) for  i in range(1, 21) if i % 2 == 0]  # поменяли на (i, f(i))
print(list4) # вывод: [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]