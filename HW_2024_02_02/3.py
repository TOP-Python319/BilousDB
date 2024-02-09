# Написать программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

# В этой задаче НУЖНО использовать f-строки.

# Пример ввода:
#     150

# Пример вывода:
#     150 мин - это 2 час 30 мин

time_in_minutes = int(input('Enter time in minutes: '))

hours = time_in_minutes // 60
minutes = time_in_minutes % 60

print(f"{time_in_minutes} minutes - is {hours} hours {minutes} minutes")

# Ввод и вывод:
# Enter time in minutes: 150
# 150 minutes - is 2 hours 30 minutes