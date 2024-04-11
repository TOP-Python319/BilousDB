# Написать программу, которая переименовывает дублирующиеся файлы.

# Это задача, которую решает каждая операционная система при поптыке размещения одноимённых файлов в одном каталоге.

# Программа получает из stdin строку, содержащую имена файлов, разделённые точкой с запятой и символом пробела (см. пример ввода).

# Далее программа генерирует новые имена для повторяющихся файлов.
    
#     Первый из одноимённых файл остаётся со своим исходным именем.
#     Начиная со второго из одноимённых файла программа добавляет в имя файла перед расширением постфикс "_n", где n — количество раз, сколько такое имя файла уже встречалось.

# Программа выводит в stdout отсортированные по алфавиту новые имена файлов, каждое имя на отдельной строке (см. пример вывода).

# Примечание 1: расширение файла является частью имени, таким образом файлы a.txt и a.py не являются одноимёнными и могут без конфликта находиться в одном каталоге.

# Примечание 2: расширения бывают составными, например .tar.gz

# Пример ввода:
#     1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.py; src.tar.gz

# Пример вывода:
#     1.py
#     1_2.py
#     1_3.py
#     aux.h
#     functions.h
#     main.cpp
#     main_2.cpp
#     main.py
#     src.tar.gz
#     src_2.tar.gz

def rename_duplicates(files):
    # Словарь для хранения количества имен файлов
    counts = {}
    # Результирующий список переименованных файлов
    result = []

    for file in files:
        # Разбиваем имя файла на базовое имя и расширение
        base_name, extension = file.rsplit('.', 1)
               
        # Проверяем еще раз, есть ли точка, для учета составных расширений
        last_dot_index = base_name.rfind('.')
        if last_dot_index > 0:
            parts = base_name.rsplit('.', 1)           # Если точка найдена, то разбиваем имя файла еще раз
            base_name = parts[0]
            extension = parts[1] + '.' + extension     # Добавляем новую часть расширения через точку
        
        # Проверяем, сколько раз мы уже встречали это имя файла
        # if file in counts:
        #     count = counts[file] + 1
        #     counts[file] += 1
        # else:
        #     count = 1
        #     counts[file] = 1
        if not file in counts:
            counts[file] = 1
        else:
            counts[file] += 1

        # Формируем новое имя файла
        count = counts[file]
        new_name = f"{base_name}_{count}.{extension}" if count > 1 else file
        result.append(new_name)

    return result

if __name__ == "__main__":
    # Вводные данные
    files = input().strip().split("; ")
    # Вызываем функцию 
    renamed_files = rename_duplicates(files)
    # Сортируем и выводим результат
    for file in sorted(renamed_files):
        print(file)

# Ввод 1:
#     1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.py; src.tar.gz

# Вывод 1:
#     1.py
#     1_2.py
#     1_3.py
#     aux.h
#     functions.h
#     main.cpp
#     main.py
#     main_2.cpp
#     src.tar.gz
#     src_2.tar.gz



# Комментарии преподавателя:
# Использовать конструкцию if not file in counts: counts[file] = 1, т.к. это более эффективно, чем if file not in counts: counts[file] = 1

# Код скорректирован в соответствии с комментариями