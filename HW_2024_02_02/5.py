# Написать программу, преобразовывающую мили в километры.

# Программа должна получить от пользователя целую и дробную часть числа миль за два ввода: см. пример ниже.
# После проведения вычисления необходимо вывести строку с результатами, как в примере ниже. Значение километров должно быть математически округлено до одного знака в десятичной части.

# Используйте следующее соотношение: 1 миля = 1.61 км

# Для округления можно использовать встроенную функцию round(). Информация о её использовании в документации:
#     https://docs.python.org/3/library/functions.html

# Также, для округления можно использовать синтаксис f-строк:
#     >>> f'{12.358:.2f}'
#     '12.36'
#     >>> f'{12.358:.1f}'
#     '12.4'

# Пример ввода:
#     15
#     7

# Пример вывода:
#     15.7 миль = 25.3 км

miles_whole = int(input("Enter the whole part of miles: "))
miles_fractional = int(input("Enter the fractional part of miles: "))

miles = miles_whole + miles_fractional / 10
kilometers = miles * 1.61

print(f"{miles_whole}.{miles_fractional} miles = {kilometers:.1f} km")

# Ввод и вывод:
# Enter the whole part of miles: 15
# Enter the fractional part of miles: 7
# 15.7 miles = 25.3 km
