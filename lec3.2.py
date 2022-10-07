# def sum(x, y):
#     return x + y

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    #print(op(a, b))
#calc(mult, 4, 5)

#f = sum  # в переменную передали ссылку на ф-ю
f = lambda q, w: q + w # lambda - ключевое слово, суть та же, что ф-я sum: sum = lambda x, y: x + y
#sum = lambda x, y: x + y + 1
#calc(sum, 4, 5)

calc(lambda x, y: x + y, 4, 5) # передали в к-ве аргумента lambda x, y: x + y, откинов классическую ф-ю и переменную с типом function