# DICT - словарь - неупорядоченные коллекции произвольных объектов с доступом по ключу.
dictionary = {}         # Пустой словарь, обратный слэш "\" нужен, чтоб не писать всё в одну строчку.
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)          # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left'])   # ←

for k in dictionary.keys():
    print(k)
for v in dictionary.values():
    print(v)
print('-' * 50)
for v in dictionary:
    print(dictionary[v])
print('-' * 50)
for i in dictionary:                      #for (k, v) in dictionary.items():
    print('{}:{}'.format(i, dictionary[i]))




# Для написания стрелки вправо (→) следует одной рукой нажать клавишу Alt и, удерживая её,
# другой рукой ввести на Num-клавиатуре цифры 2 6. Отпустите Alt — получится стрелка вправо
# Для стрелки влево (←) работает комбинация Alt и 2 7
# Вниз (↓) — Alt и 2 5
# Вверх (↑) — Alt и 2 4
# Вверх-вниз (↕) — Alt и 1 8
# Влево-вправо (↔) — Alt и 2 9