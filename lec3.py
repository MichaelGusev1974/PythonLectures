def f(x):
    return x**2

g = f   # переменная, которая хранит ссылку на функцию f
print(type(f))  # вывод <class 'function'>
print(type(g))  # вывод <class 'function'>
print(f(2))
print(g(4))

