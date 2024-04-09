# Написать программу, которая проверяет корректность хода шахматной ладьи.
# Программа должна по очереди получить из stdin координаты двух клеток шахматной доски.
# Программа должна вывести в stdout “да”, если из первой клетки можно попасть во вторую одним ходом ладьи. В противном случае должно быть выведено “нет”.
# Примечание: шахматная ладья ходит по горизонтали или вертикали.

# Пример ввода 1:
#     d4
#     e4

# Пример вывода 1:
#     да

# Пример ввода 2:
#     a2
#     c4

# Пример вывода 2:
#     нет

# Получаем координаты двух клеток от пользователя
first_coordinate = input()
second_coordinate = input()

# Извлекаем координаты столбцов и строк для обеих клеток
col_first = first_coordinate[0]
row_first = first_coordinate[1]
col_second = second_coordinate[0]
row_second = second_coordinate[1]

# Проверяем, находятся ли клетки на одной вертикали или горизонтали
if col_first == col_second or row_first == row_second:
    print("да")
else:
    print("нет")

# Ввод и вывод 1:
#     d4
#     e4
#     да

# Ввод и вывод 2:
#     a2
#     c4
#     нет


# всё чисто, вопросов нет. =)