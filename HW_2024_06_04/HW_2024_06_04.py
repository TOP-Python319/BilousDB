# Создать систему управления библиотекой.
# Библиотека состоит из отделов
# (например, отдел художественной литературы, отдел научной литературы и т.д.).
# В каждом отделе есть свой набор книг.
# Книги могут перемещаться между отделами.
# Читатели могут брать книги в отделе и возвращать их обратно.



# Было дополнительно реализовано:
#       - два пользовательских класса ошибок - BookNotFoundError и BookAlreadyExistsError, 
#         чтобы обрабатывать ситуации, когда книга не найдена в отделе или уже существует в отделе.
#       - метод find_book в классе Library, который позволяет искать книгу по названию во всех отделах библиотеки. 
#         Если книга не найдена, поднимается исключение BookNotFoundError.
#       - класс Reader, который позволяет читателям брать книги из библиотеки и возвращать их обратно. 
#         В этом классе используется метод is_available из класса Book, чтобы определить доступна ли книга для взятия.
#       - При создании нового объекта класса Reader, мы передаем ему имя читателя и уникальный номер читательского билета.
#         Читательский билет используется для идентификации конкретного читателя. 
#         Этот идентификатор позволяет системе библиотеки отслеживать, какие книги взяты каждым читателем, 
#         чтобы обеспечить правильное управление книгами и предотвратить конфликты взятия одной книги несколькими читателями одновременно.
#       - Также теперь при вызове метода __str__ у Library мы можем видеть у какого читателя находится книга.


from dataclasses import dataclass

class BookNotFoundError(Exception):
    """Исключение, выбрасываемое когда книга не найдена в департаменте."""
    def __init__(self, book_name, department_name):
        self.message = f'Книга "{book_name}" не найдена в департаменте "{department_name}".'
        super().__init__(self.message)

class BookAlreadyExistsError(Exception):
    """Исключение, выбрасываемое при попытке добавить книгу, которая уже существует в отделе."""
    def __init__(self, book_name, department_name):
        self.message = f'Книга "{book_name}" уже существует в отделе "{department_name}".'
        super().__init__(self.message)
    

@dataclass
class Book:
    name: str
    author: str
    pages: int
    year: int
    is_available: bool = True
    reader_id: str = None  # номер читательского билета читателя, который взял книгу

    def take(self, reader):
        if self.is_available:
            self.is_available = False
            self.reader_id = reader.reader_id
        else:
            raise ValueError(f'Книга "{self.name}" недоступна на данный момент, т.к. уже была взята')

    def return_back(self):
        if not self.is_available:
            self.is_available = True
            self.reader_id = None
        else:
            raise ValueError(f'Книгу "{self.name}" невозможно вернуть. Книга уже находится в библиотеке')


class Library:
    class Department:
        def __init__(self, name: str):
            self.name = name
            self.books = []

        def __str__(self):
            result = f'Отдел {self.name} имеет книги:'
            for book in self.books:
                status = "доступна" if book.is_available else f"на руках у читателя с номером {book.reader_id}"   # добавлен статус книги
                result += f'\n{book.name} автора {book.author}, {status}'
            return result

        def add_book(self, book: Book):
            if any(b.name == book.name for b in self.books):
                raise BookAlreadyExistsError(book.name, self.name)
            self.books.append(book)

        def del_book(self, book: Book):
            try:
                self.books.remove(book)
            except ValueError:
                raise BookNotFoundError(book.name, self.name)

    def __init__(self, name: str):
        self.name = name
        self.departments = {}

    def __str__(self):
        result = f'{self.name} имеет отделы:\n'
        for department in self.departments:
            result += f'\t{department}:\n'
            for book in self.departments[department].books:
                status = "доступна" if book.is_available else f"на руках у читателя с номером {book.reader_id}"
                result += f'\t\t{book.name} автора {book.author}, {status}\n'
        return result

    def add_department(self, name: str):
        self.departments[name] = self.__class__.Department(name)

    def move_book(self,
                  book: Book,
                  department_from: Department,
                  department_to: Department):
        department_from.del_book(book)
        department_to.add_book(book)

    def find_book(self, book_name: str) -> Book:
        """
        Метод, который ищет книгу в библиотеке по названию
        Возвращает книгу, в противном случае поднимает ошибку, что книга не найдена ни в одном департаменте"""
        for department in self.departments.values():
            for book in department.books:
                if book.name == book_name:
                    return book
        raise BookNotFoundError(book_name, "any department")

class Reader:
    """
    Класс читателя.
    Аргументы:
    name(str) - имя читателя
    reader_id(str) - номер читательского билета
    self.borrowed_books(list) - список книг, которые взял читатель
    """
    def __init__(self, name: str, reader_id: str) -> None:
        self.name = name
        self.reader_id = reader_id   
        self.borrowed_books = []      
    
    def borrow_book(self, library: Library, book_name: str):
        try:
            book = library.find_book(book_name)       # проверяем существует ли такая книга в библиотеке
        except BookNotFoundError as e:
            print(e)
            return
        if book.is_available:
            book.take(self)
            self.borrowed_books.append(book)
        else:
            raise ValueError(f'Книга "{book_name}" сейчас недоступна. Скорее всего она взята другим читателем')
    
    def return_book(self, library: Library, book_name: str):
        book = next((b for b in self.borrowed_books if b.name == book_name), None)
        if book:
            book.return_back()
            self.borrowed_books.remove(book)
        else:
            raise ValueError(f'Книга "{book_name}" не была взята читателем {self.name}.')

    def __str__(self):
        return f'Читатель {self.name} (Читательский билет: {self.reader_id}) взял книги: {[book.name for book in self.borrowed_books]}'


library = Library('Ленинская библиотека')
FICTION_BOOKS = 'Художественная литература'
SCIENCE_BOOKS = 'Научная литература'
library.add_department(FICTION_BOOKS)
library.add_department(SCIENCE_BOOKS)

brave_new_world = Book('Brave New World', 'Aldous Huxley', 311, 1932)
anna_karenina = Book('Anna Karenina', 'Leo Tolstoy', 864, 1877)
fight_club = Book('Fight Club', 'Chuck Palahniuk', 366, 1996)
universe_in_a_nutshell = Book('Universe in a nutshell', 'Stephen Hawking', 480, 1976)

library.departments[FICTION_BOOKS].add_book(brave_new_world)
library.departments[FICTION_BOOKS].add_book(anna_karenina)
library.departments[FICTION_BOOKS].add_book(fight_club)
library.departments[FICTION_BOOKS].add_book(universe_in_a_nutshell)

library.move_book(universe_in_a_nutshell, library.departments[FICTION_BOOKS], library.departments[SCIENCE_BOOKS])

# anna_karenina.take() # TypeError: take() missing 1 required positional argument: 'reader'

print(library)
# Вывод:
# Ленинская библиотека имеет отделы:
#         Художественная литература:
#                 Brave New World автора Aldous Huxley, доступна
#                 Anna Karenina автора Leo Tolstoy, доступна
#                 Fight Club автора Chuck Palahniuk, доступна
#         Научная литература:
#                 Universe in a nutshell автора Stephen Hawking, доступна


# Проверка класса Reader:
# создаем читателя и пытаемся взять книгу
reader_alex = Reader('Alex', 'Reader123')
reader_alex.borrow_book(library, 'Anna Karenina')

print(library)
# Вывод:
# Ленинская библиотека имеет отделы:
#         Художественная литература:
#                 Brave New World автора Aldous Huxley, доступна
#                 Anna Karenina автора Leo Tolstoy, на руках у читателя с номером Reader123
#                 Fight Club автора Chuck Palahniuk, доступна
#         Научная литература:
#                 Universe in a nutshell автора Stephen Hawking, доступна


# пытаемся взять книгу, которая отсутствует в библиотеке
reader_alex.borrow_book(library, '1984')  
# Вывод: Книга "1984" не найдена в департаменте "any department".

# Пытаемся вернуть книгу, которую не взяли
try:
    reader_alex.return_book(library, '1984')
except ValueError as e:
    print(e)  # Вывод: Книга "1984" не была взята читателем Alex.

# Пытаемся взять еще одну книгу
reader_alex.borrow_book(library, 'Universe in a nutshell')

# Выводим книги которые взял наш читатель
print(reader_alex)
# Вывод: Читатель Alex (Читательский билет: Reader123) взял книги: ['Anna Karenina', 'Universe in a nutshell']

# Возвращаем книгу читателя Alex 
reader_alex.return_book(library, 'Anna Karenina')
print(reader_alex)
# Вывод: Читатель Alex (Читательский билет: Reader123) взял книги: ['Anna Karenina']

print(library)
# Вывод: 
# Ленинская библиотека имеет отделы:
#   Художественная литература:
#         Brave New World автора Aldous Huxley, доступна
#         Anna Karenina автора Leo Tolstoy, доступна
#         Fight Club автора Chuck Palahniuk, доступна
#   Научная литература:
#         Universe in a nutshell автора Stephen Hawking, на руках у читателя с номером Reader123


# Попытка добавить книгу, которая уже существует в отделе
try:
    library.departments[FICTION_BOOKS].add_book(brave_new_world)
except BookAlreadyExistsError as e:
    print(e)  
# Вывод: Книга "Brave New World" уже существует в отделе "Художественная литература".


# Пытаемся взять книгу, которая уже взята другим читателем
reader_john = Reader('John', 'Reader456')
reader_john.borrow_book(library, 'Anna Karenina')

try:
    reader_alex.borrow_book(library, 'Anna Karenina')
except ValueError as e:
    print(e)  # Вывод: Книга "Anna Karenina" сейчас недоступна. Скорее всего она взята другим читателем

print(library)

# Вывод:
# Ленинская библиотека имеет отделы:
#         Художественная литература:
#                 Brave New World автора Aldous Huxley, доступна
#                 Anna Karenina автора Leo Tolstoy, на руках у читателя с номером Reader456
#                 Fight Club автора Chuck Palahniuk, доступна
#         Научная литература:
#                 Universe in a nutshell автора Stephen Hawking, на руках у читателя с номером Reader123


# Проверка других пользовательских исключений:

# Попытка добавить книгу, которая уже существует в отделе
# library.departments[FICTION_BOOKS].add_book(brave_new_world)
# Вывод: __main__.BookAlreadyExistsError: Книга "Brave New World" уже существует в отделе "Художественная литература".

# Попытка удалить книгу, которая не существует в отделе
# non_existing_book = Book('Non-existing Book', 'Unknown Author', 100, 2023)
# library.departments[FICTION_BOOKS].del_book(non_existing_book)
# Вывод: __main__.BookNotFoundError: Книга "Non-existing Book" не найдена в департаменте "Художественная литература".




