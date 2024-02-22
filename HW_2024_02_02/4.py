# Написать программу, в которой рассчитываются сумма и произведение цифр положительного трёхзначного числа.

# Число должно быть введено слитно за один раз, как в примере ниже.

# Для забегающих вперёд: использование индексации по строке зачтено не будет. Найдите способ выполнить задачу используя только уже полученный материал.

# Пример ввода:
#     333

# Пример вывода:
#     Сумма цифр = 9
#     Произведение цифр = 27

number = int(input('Enter a three-digit number: '))

# Извлекаем цифры из числа
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

# Рассчитываем сумму и произведение цифр
digit_sum = first_digit + second_digit + third_digit
digit_product = first_digit * second_digit * third_digit

# Выводим результат
print(f"Sum of digits = {digit_sum}")
print(f"Product of digits = {digit_product}")

# Ввод и вывод:
# Enter a three-digit number: 333
# Sum of digits = 9
# Product of digits = 27

# комментарий преподавателя:
# всё чисто, вопросов нет. =)