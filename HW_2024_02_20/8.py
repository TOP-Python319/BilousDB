# Написать программу, которая требуемое количество чисел последовательности Фибоначчи.

# Программа получает из stdin натуральное число n. 
# Далее, программа считает и выводит в stdout n чисел последовательности Фибоначчи.

# Примечание: последовательность Фибоначчи — это последовательность натуральных чисел, которая начинается с двух единиц, а каждое последующее число является суммой двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …

# Пример ввода 1:
#     1
# Пример вывода 1:
#     1

# Пример ввода 2:
#     17
# Пример вывода 2:
#     1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

n = int(input('Введите количество чисел последовательности Фибоначчи: '))

fib_sequence = [1, 1]

for i in range(2, n):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

print(*fib_sequence)

# Ввод 1:
# Введите количество чисел последовательности Фибоначчи: 1
# Вывод 1:
# 1 1

# Ввод 2:
# Введите количество чисел последовательности Фибоначчи: 17
# Вывод 2:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

#####
# Комментарий преподавателя:
# Всё правильно!