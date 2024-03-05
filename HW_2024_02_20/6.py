# Написать программу, которая проверяет транспортный билет.

# Отрывные билеты старого формата в наземном общественном транспорте содержали номер из шести цифр. Билетик считался «счастливым», если сумма первых трёх цифр совпадала с суммой последних трёх цифр.

# Пример ввода 1:
#     183534

# Пример вывода 1:
#     да

# Пример ввода 2:
#     401367

# Пример вывода 2:
#     нет

ticket_number = input('Введите шестизначный номер билета: ')

first_half = ticket_number[:3]
second_half = ticket_number[3:]

first_half_digits = [int(digit) for digit in first_half]
second_half_digits = [int(digit) for digit in second_half]

if sum(first_half_digits) == sum(second_half_digits):
    print('да')
else:
    print('нет')

# Ввод 1:
#     183534
# Вывод 1:
#     да

# Ввод 2:
#     401367
# Вывод 2:
#     нет






