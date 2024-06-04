# #1 (Пользовательские исключения)

# Нужно реализовать базовый класс исключения PasswordInvalidError,
# который наследуется от стандартного класса исключений Exception.

# Этот класс можно использовать для обработки любых общих ошибок, связанных с неверными паролями.

# От него нужно унаследовать следующие классы:
#     PasswordLengthError представляет ошибку, связанную с недостаточной длиной пароля;
#     PasswordContainUpperError представляет ошибку, связанную с отсутствием заглавных букв в пароле;
#     PasswordContainDigitError представляет ошибку, связанную с отсутствием цифр в пароле.
 
# Создайте класс User с атрибутами username и password(пароль по умолчанию None).
# Класс должен иметь метод set_password,
# который принимает пароль и устанавливает его как значение атрибута password.

# Метод set_password должен также проверять,
# соответствует ли пароль заданным требованиям безопасности:
#     Длина пароля должна быть не менее 8 символов(в противном случае генерируется исключение PasswordLengthError с текстом Пароль должен быть не менее 8 символов);
#     Пароль должен содержать хотя бы одну заглавную букву (в противном случае генерируется исключение PasswordContainUpperError с текстом Пароль должен содержать хотя бы одну заглавную букву);
#     Пароль должен содержать хотя бы одну цифру (в противном случае генерируется исключение PasswordContainDigitError с текстом Пароль должен содержать хотя бы одну цифру);


class PasswordInvalidError(Exception):
    """Базовый класс для других исключений"""
    

class PasswordLengthError(PasswordInvalidError):
    """Исключение в случае, если пароль недостаточной длины"""
    def __str__(self) -> str:
        return 'Пароль должен быть не менее 8 символов'


class PasswordContainUpperError(PasswordInvalidError):
    """Исключение в случае, если в пароле отсутствуют заглавные буквы"""
    def __str__(self) -> str:
        return 'Пароль должен содержать хотя бы одну заглавную букву'


class PasswordContainDigitError(PasswordInvalidError):
    """Исключение в случае, если в пароле отсутствуют цифры"""
    def __str__(self) -> str:
        return 'Пароль должен содержать хотя бы одну цифру'


class User:
    """Пользовательский класс"""
    def __init__(self, username: str, password: str=None) -> None:
        """
        Метод-конструктор, инициализирует пользователя.
        Аргументы:
            username(str): Имя пользователя.
            password(str): Пароль пользователя (по умолчанию None).
        """
        self.username = username
        self.password = password
    
    def set_password(self, password: str) -> None:
        """
        Устанавливает пароль пользователя после проверки его на соответствие требованиям.
        Args:
            password(str): Пароль, который нужно установить.
        Raises:
            PasswordLengthError: Если длина пароля меньше 8 символов.
            PasswordContainUpperError: Если пароль не содержит заглавных букв.
            PasswordContainDigitError: Если пароль не содержит цифр.
        """
        if len(password) < 8:
            raise PasswordLengthError()
        elif not any(char.isupper() for char in password):
            raise PasswordContainUpperError()
        elif not any(char.isdigit() for char in password):
            raise PasswordContainDigitError()
        self.password = password


# Ниже код для проверки

assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)   

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'

# Вывод:
# Пароль должен быть не менее 8 символов
# Пароль должен содержать хотя бы одну заглавную букву
# Пароль должен содержать хотя бы одну цифру



