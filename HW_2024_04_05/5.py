# Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

# Примечание 1. Исполняемая программа и указанные файлы находятся в одной папке.
# Примечание 2. Используйте встроенную функцию enumerate().
# Примечание 3. Если бы файл input.txt содержал строки:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# то файл output.txt имел бы вид:
# 1) Beautiful is better than ugly.
# 2) Explicit is better than implicit.
# 3) Simple is better than complex.
# 4) Complex is better than complicated.

with open('input.txt', 'r', encoding='utf-8') as file_1:  # Открываем первый файл для чтения
    lines = file_1.readlines()                            # Считываем строки из первого файла
with open('output.txt', 'w', encoding='utf-8') as file_2: # Открываем второй файл для записи
    for i, line in enumerate(lines, start=1):             # Проходимся по строкам из первого файла с циклом
        file_2.write(f'{i}) {line}')                      # Записываем пронумерованные строки во второй файл

# Вывод в файле output.txt
# 1) abcd
# 2) xcnvmnvkje
# 3) 32432423
# 4) sdflsdjkn34r43
# 5) 345349854395#$%$#
# 6) jksdfkjsdfkjsd
# 7) lwerjlwerlkwe
# 8) jwfhjkwehkjwefkjwebfjkwe
# 9) djdddddddddddddddddddddddddddddddd
# 10) 3249835438594390583490583490853490582349058340
# 11) sdfsjkldflksdjaflkjsdflkjsdlfkjsdlfjsldfsldkfjlsdkfjls


# комментарий преподавателя:
# всё верно

