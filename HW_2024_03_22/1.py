# Написать функцию с именем strong_password, которая проверяет, является ли пароль надёжным.

# Функция принимает обязательным позиционно-ключевым аргументом пароль в виде объекта str.

# Функция возвращает объект bool.

# Пароль считается надёжным, если соблюдены все нижеследующие условия:
#     - длина пароля составляет восемь символов и более
#     - в пароле присутствуют буквенные символы в обоих регистрах
#     - в пароле присутствуют минимум два символа цифр
#     - кроме символов букв и цифр в пароле присутствуют символы прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.)

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> strong_password('aP3:kD_l3')
#     True
#     >>> strong_password('password')
#     False

def strong_password(password: str) -> bool:
    # длина пароля составляет восемь символов и более
    if len(password) < 8:
        return False
    # в пароле присутствуют буквенные символы в обоих регистрах
    if not any(char.islower() for char in password) or not any(char.isupper() for char in password):
        return False
    # в пароле присутствуют минимум два символа цифр
    if sum(char.isdigit() for char in password) < 2:
        return False
    # кроме символов букв и цифр в пароле присутствуют символы прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.)
    if password.isalnum():
        return False
    # или
    return True
    
print(strong_password('aP3:kD_l3'))  # True
print(strong_password('password'))   # False