# Написать программу, которая принимает пользовательский ввод только до тех пор пока он соответствует условию.

# Программе в цикле получает из стандартного потока ввода (stdin) по одному целому числу, кратному семи. При появлении любого числа, не делящегося на семь, цикл прерывается. 
# После окончания цикла программа выводит в stdout в одну строку все числа кратные семи в обратном порядке.

# Пример ввода:
#     7
#     7
#     14
#     21
#     13

# Пример вывода:
#     21 14 7 7

result = []

while True:
    number = int(input('Введите число, кратное 7: '))
    if number % 7 == 0:
        result.append(number)
    else:
        break

print(' '.join(map(str, reversed(result))))
# формально правильно, мы получили строку содержащую ответ, но можно было сделать проще и быстрее
# print(*reversed(result), sep=' ')
# таким образом мы не делаем приведение типов и не склеиваем строку.
# -2 операции

# Ввод и вывод:
# Введите число, кратное 7: 7
# Введите число, кратное 7: 7
# Введите число, кратное 7: 14
# Введите число, кратное 7: 21
# Введите число, кратное 7: 13
# 21 14 7 7

#####
# Комментарий преподавателя:

# Смотрите print(), я его упростил.

# Вы изучили функцию map() самостоятельно!
# Хвалю.