# Написать программу, которая считывает целое число. Программа должна вывести следующее и предыдущее целое число с пояснительным текстом.

# Для вывода использовать один вызов функции print. 
# В этой задаче МОЖНО использовать f-строки.

# Пример ввода:
#     20

# Пример вывода:
#     Следующее за числом 20 число: 21
#     Для числа 20 предыдущее число: 19

number = int(input('Enter the integer: '))

print(f"The next number after {number} is: {number + 1}\nThe previous number for {number} is: {number - 1}")

# Ввод и вывод:
# Enter the integer: 20
# The next number after 20 is: 21
# The previous number for 20 is: 19