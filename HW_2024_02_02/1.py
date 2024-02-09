# Написать программу для сбора данных о пользователе.

# В первой строке попросить пользователя ввести имя.
# Во второй строке попросить пользователя ввести фамилию.
# В третьей строке попросить пользователя ввести год рождения.

# Программа должна вывести сначала фамилию, потом имя, затем возраст пользователя. 
# Возраст — число лет — считать без учёта дня и месяца рождения.
# Соблюсти формат вывода, показанный в примере ниже.

# Для вывода использовать один вызов функции print. 
# В этой задаче НЕ использовать f-строки.

# Пример ввода:
#     Введите имя: Иван
#     Введите фамилию: Петров
#     Введите год рождения: 2009

# Пример вывода:
#     Петров Иван, 12

name = input('Enter your name: ')
surname = input('Enter your surname: ')
year_of_birth = int(input('Enter your year of birth: '))

age = str(2024 - year_of_birth)

print(name + ' ' + surname + ', ' + age)

# Ввод и вывод:
# Enter your name: Diana
# Enter your surname: Bilous
# Enter your year of birth: 1993
# Diana Bilous, 31


