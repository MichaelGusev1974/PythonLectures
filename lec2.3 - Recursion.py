# Рекурсия - функция, вызывающая сама себя, главное указать момент, когда нужно отановиться и перестать её вызывать.
def Fib(n):
    if n in [1, 2]:                  # если n содержится в списке, состоящем из двух элементов 1 или 2, возвращаем 1
        return 1
    else:                            # иначе
        return Fib(n-1) + Fib(n - 2) # возвращаем рекурсивный вызов для n-1  и n-2

list = []
for i in range(1, 10):
    list.append(Fib(i))
print(list)