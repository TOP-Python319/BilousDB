# Написать программу, которая проверяет делится ли одно число на другое нацело. 

# Два целых числа программа должна по очереди получить из stdin (пользовательский ввод).
# Необходимо соблюсти формат вывода, показанный в примере ниже.

# В этой задаче и далее можно использовать f-строки.

# Пример ввода 1:
#     8
#     2

# Пример вывода 1:
#     8 делится на 2 нацело
#     частное: 4

# Пример ввода 2:
#     10
#     3

# Пример вывода 2:
#     10 не делится на 3 нацело
#     неполное частное: 3
#     остаток: 1


first_int = int(input())
second_int = int(input())

if first_int % second_int == 0:
    print(f"{first_int} делится на {second_int} нацело")
    print(f"частное: {first_int // second_int}")
else:
    print(f"{first_int} не делится на {second_int} нацело")
    print(f"неполное частное: {first_int // second_int}")
    print(f"остаток: {first_int % second_int}")

# Ввод 1:
# 8
# 2
# Вывод 1:
# 8 делится на 2 нацело
# частное: 4
    
# Ввод 2:
# 10
# 3
# Вывод 2:
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1


# комментарий преподавателя:
# всё чисто, вопросов нет. =)
