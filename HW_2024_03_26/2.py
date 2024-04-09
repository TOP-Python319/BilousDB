# Представьте, что у нас есть список целых чисел неограниченной вложенности.
# То есть наш список может состоять из списков, внутри которых также могут быть списки.
# Ваша задача превратить все это в линейный список при помощи функции flatten

# Вход
# [1, [2, 3, [4]], 5]
# Выход
# [1, 2, 3, 4, 5]

# Вход
# [1, [2, 3], [[2], 5], 6]
# Выход
# [1, 2, 3, 2, 5, 6]

# Вход
# [[[[9]]], [1, 2], [[8]]]
# Выход
# [9, 1, 2, 8]

def flatten(s: list) -> list:
    result = []
    for i in s:
        if isinstance(i, list):     # Проверяем, если элемент является списком
            result.extend(flatten(i)) # Eсли элемент является списком, то функция вызывает саму себя для этого элемента
        else:
            result.append(i)   # Если элемент не является списком, то срабатывает базовый случай и элемент записывается в результат
    return result


print(flatten([1, [2, 3, [4]], 5]))
# [1, 2, 3, 4, 5]
print(flatten([1, [2, 3], [[2], 5], 6]))
# [1, 2, 3, 2, 5, 6]
print(flatten([[[[9]]], [1, 2], [[8]]]))
# [9, 1, 2, 8]


# Отличная работа! Код правильно работает и хорошо написан.