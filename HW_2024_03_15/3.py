# Написать программу, которая проверяет, является ли один список частью другого списка.

# Программа два раза получает из stdin произвольное количество целых чисел, разделённых пробелом. Из каждого ввода формируется отдельный список объектов int.

# Далее, программа определяет, можно ли из первого списка выбрать срез с шагом по умолчанию (единица) так, чтобы получился второй список.
#     В решении не обязательно использовать именно срезы, есть много разных способов.

# Программа выводит в stdout текстовый ответ.

# Примечание: пустой список является частью любого списка, включая пустой.

# Пример ввода 1:
#     1 2 3 4
#     1 2

# Пример вывода 1:
#     да

# Пример ввода 2:
#     1 2 3 4
#     2 4

# Пример вывода 2:
#     нет


def is_slice_possible(list1, list2):
    """
    Проверяет, можно ли из первого списка выбрать срез с шагом по умолчанию (единица) так, чтобы получился второй список.

    Аргументы:
    list1: список целых чисел - первый список
    list2: список целых чисел - второй список

    Возвращает:
    bool: True, если можно выбрать срез из первого списка, чтобы получился второй список, иначе False.
    """
    len1, len2 = len(list1), len(list2) # Определяем длины обоих списков
    for i in range(len1 - len2 + 1):    # Перебираем возможные начальные индексы для среза
        if list1[i:i+len2] == list2:    # Проверяем, соответствует ли срез второму списку
            return True
    return False

# Получаем ввод данных
first_inp = input('Enter an arbitrary number of integers separated by space: ')
second_inp = input('Enter an arbitrary number of integers separated by space: ')

# Преобразуем введенные строки в списки целых чисел
first_input_list = [int(num) for num in first_inp.split()]
second_input_list = [int(num) for num in second_inp.split()]

# Вызываем функцию и сохраняем результат в переменной
result = is_slice_possible(first_input_list, second_input_list)

if result:
    print('yes')
else:
    print('no')


# Ввод 1:
#     Enter an arbitrary number of integers separated by space: 1 2 3 4  
#     Enter an arbitrary number of integers separated by space: 1 2  
# Вывод 1:
#     yes

# Ввод 2:
#     Enter an arbitrary number of integers separated by space: 1 2 3 4
#     Enter an arbitrary number of integers separated by space: 2 4
# Вывод 2:
#     no

# Ввод 3:
#     Enter an arbitrary number of integers separated by space: 1 2 3 4 5 6 7 8 
#     Enter an arbitrary number of integers separated by space: 4 5 6
# Вывод 3:
#     yes

# Ввод 4:
#     Enter an arbitrary number of integers separated by space: 1 2 3 4 5 6 7
#     Enter an arbitrary number of integers separated by space: 4 6 7
# Вывод 4:
#     no



# Комментарии преподавателя:
# все верно