# Написать функцию с именем int_base, которая преобразовывает число из произвольной системы счисления в произвольную.

# Функция принимает обязательными аргументами строковую запись числа, основание исходной системы счисления и основание целевой системы счисления.
    
#     Все аргументы должны быть позиционно-ключевыми.
    
#     Преобразовываемое число принимается в виде объекта str.
    
#     Основания систем счисления принимаются в виде объектов int, в диапазоне от 2 до 36 включительно.
#         Для записи дополнительных цифр в системах счисления с основанием больше десяти используйте латинские буквы от 'a' до 'z'. Имеет смысл сгенерировать словарь, задающий соотношения между числами в десятичной системе счисления и цифрами в системах счисления с бо́льшим основанием.
#         Следите за регистром буквенных символов.

# Функция возвращает строковое представление числа в целевой системе счисления или None в случае возникновения ошибок.

#     Ошибки могут возникать в следующих случаях:
#         - исходное или целевое основание системы счисления находится за пределами обозначенного выше диапазона
#         - строковое представление числа не соответствует заявленной исходной системе счисления
    
# Преобразования такого рода можно производить напрямую, но это потребует более сложной математики. В рамках данной задачи имеет смысл реализовать двойное преобразование: из исходной системы счисления в десятичную и затем из десятичной системы счисления в целевую. 

#     Представляется целесообразным каждое из этих двух преобразований реализовать в виде отдельной функции. Продумайте самостоятельно сигнатуры этих функций (набор параметров, их типы, возвращаемые значения).
    
#     О математике преобразований между системами счисления:
#         http://math-info.hse.ru/a/2021-22/ling-dm/lectures/lecture9_delim.pdf

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> int_base('ff00', 16, 2)
#     '1111111100000000'
#     >>> int_base('1101010', 2, 30)
#     '3g'

def conversion_to_decimal(number: str, base: int) -> int | None:
    """
    Преобразует число из произвольной системы счисления в десятичную.

    Принимает:
        number (str): Строковое представление числа в исходной системе счисления.
        base (int): Основание исходной системы счисления.

    Возвращает:
        int | None: Десятичное число, если преобразование удалось, иначе None.
    """
    # Проверяем основание системы счисления
    if not 2 <= base <= 36:
        return None
    
    # Преобразуем число в десятичную систему счисления
    decimal_number = int(number, base)
    return decimal_number


def conversion_from_decimal(decimal_number: int, base: int) -> str | None:
    """
    Преобразует десятичное число в произвольную систему счисления.

    Принимает:
        decimal_number (int): Десятичное число.
        base (int): Основание целевой системы счисления.

    Возвращает:
        str | None: Строковое представление числа в нужной нам системе счисления, если преобразование удалось, иначе None.
    """
    # Проверяем основание системы счисления
    if not 2 <= base <= 36:
        return None
    
    # Преобразуем десятичное число в целевую систему счисления
    converted_number = ''
    while decimal_number > 0:
        remainder = decimal_number % base
        if remainder < 10:
            converted_number = str(remainder) + converted_number
        else:
            converted_number = chr(ord('A') + remainder - 10) + converted_number
        decimal_number //= base
    return converted_number


def int_base(number: str, from_base: int, to_base: int) -> str | None:
    """
    Преобразует число из одной системы счисления в другую.

    Принимает:
        number (str): Строковое представление числа в исходной системе счисления.
        from_base (int): Основание исходной системы счисления.
        to_base (int): Основание целевой системы счисления.

    Возвращает:
        str | None: Строковое представление числа в целевой системе счисления, если преобразование удалось, иначе None.
    """
    # Преобразуем число из исходной системы счисления в десятичную
    decimal_number = conversion_to_decimal(number, from_base)
    if decimal_number is None:
        return None
    
    # Преобразуем десятичное число в целевую систему счисления
    converted_number = conversion_from_decimal(decimal_number, to_base)
    return converted_number


    
print(int_base('1111111100000000', 2, 10))
# 65280
print(int_base('ff00', 16, 2))
# 1111111100000000
print(int_base('1101010', 2, 30))
# 3G
print(int_base('869', 10, 2))
# 1101100101
print(int_base('1101100101', 2, 10))
# 869
print(int_base('1101100101', 2, 16))
# 365