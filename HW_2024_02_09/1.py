# Написать программу, которая подсчитывает сумму только положительных чисел.

# Три числа программа должна по очереди получить из пользовательского ввода (stdin — стандартный поток ввода).

# Пример ввода:
#     4
#     -22
#     1.5

# Пример вывода:
#     5.5

first_number = float(input())
second_number = float(input())
third_number = float(input())

result = 0

if first_number > 0:
    result += first_number

if second_number > 0:
    result += second_number

if third_number > 0:
    result += third_number

print(result)

# Ввод:
# 4
# -22
# 1.5
# Вывод:
# 5.5


# Комментарий преподавателя:
# можно переписать логику на более компактный вариант с использованием генератора:
result = sum(num for num in (first_number, second_number, third_number) if num > 0)
print(result)

