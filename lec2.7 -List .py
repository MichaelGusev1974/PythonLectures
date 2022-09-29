# При копировании списка, а, в процессе работы, при изменении значения элемента в одном списке - это же значение
# меняется и в копии списка. Следует быть внимательным.
list1 = [1, 2, 3, 4, 5]
list2 = list1
for i in list1:
    print(i)
print()
for i in list2:
    print(i)
print()
list1[0] = 123
list2[1] = 333

for i in list1:
    print(i)
print()
for i in list2:
    print(i)

