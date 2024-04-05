# Написать функцию с именем numbers_strip, которая удаляет n минимальных и n максимальных чисел из списка.

# Функция принимает обязательным аргументом список вещественных чисел, необязательными аргументами число n и переключатель вернуть исходный список или копию.
    
#     Список чисел должен быть позиционно-ключевым, передаётся в виде объекта list, элементами списка должны быть объекты float.
    
#     Число n должно быть позиционно-ключевым, передаётся в виде объекта int, значение по умолчанию — 1.
    
#     Переключатель должен быть строго ключевым, передаётся в виде объекта bool, значение по умолчанию False.

# Функция возвращает исходный списка с внесёнными изменениями или копию исходного списка в виде объекта list.

# Примечание: не забывайте про встроенные функции min() и max()

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> sample = [1, 2, 3, 4]
#     >>> sample_stripped = numbers_strip(sample)
#     >>> sample_stripped
#     [2, 3]

#     >>> 
#     >>> sample = [10, 20, 30, 40, 50]
#     >>> sample_stripped = numbers_strip(sample, 2, copy=True)
#     >>> sample_stripped
#     [10, 20, 30, 40, 50]

def numbers_strip(numbers_list: list[float], n: int=1, *, copy: bool=False) -> list[float]:
    # Функция возвращает исходный список в случае True
    if copy:
        return numbers_list.copy()
    # или
    else:
        for _ in range(n):
            numbers_list.remove(min(numbers_list)) # удаление минимального числа
            numbers_list.remove(max(numbers_list)) # удаление максимального числа
        return numbers_list
                 

sample = [1, 2, 3, 4]
sample_stripped = numbers_strip(sample)
print(sample_stripped)
# [2, 3]

sample = [10, 20, 30, 40, 50]
sample_stripped = numbers_strip(sample, 2, copy=True)
print(sample_stripped)
# [10, 20, 30, 40, 50]
