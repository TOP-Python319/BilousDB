# Написать программу, которая вычисляет сумму всех делителей числа.

# Программа получает из stdin натуральное число. 
# Далее, программа считает и выводит в stdout сумму делителей этого числа.

# Необходимо использовать цикл с минимально возможным количеством итераций.

# Пример ввода:
#     50

# Пример вывода:
#     93

n = int(input('Введите натуральное число: '))
sum = 0  

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        if i == n // i:
            sum += i
        else:
            sum += i + n // i

print(f'Сумма делителей числа {n} равна: {sum}')

# PS. вышло немного больше кода, но, мне кажется, что это вариант
# с наименьшим кол-вом итераций, т.к. ищем делители только до квадратного корня из n

# Ввод 1:
# Введите натуральное число: 50
# Вывод 1:
# Сумма делителей числа 50 равна: 93

# Ввод 2:
# Введите натуральное число: 36
# Вывод 2:
# Сумма делителей числа 36 равна: 91

#####
# Комментарий преподавателя:
# Да, это верная оптимизация,
# сокращая правую границу range()
# до корня из n, мы уменьшаем количество итераций
# в два раза, при этом делителей от (n ** 0.5) до n 
# просто нет.





