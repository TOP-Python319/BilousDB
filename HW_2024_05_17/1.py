# #1
# Напишите суперкласс Publisher (издательство) и два подкласса BookPublisher (книжное издательство) и NewspaperPublisher (газетное издательство).

# Родительский класс Publisher имеет два атрибута name и location (название, расположение) и два метода:
# 	get_info(self) – предоставляет информацию о названии и расположении издательства;
# 	publish(self, message) – выводит информацию об издании, которое находится в печати.

# Подклассы BookPublisher и NewspaperPublisher используют метод super().__init__(name, location) суперкласса для вывода информации о своих названии и расположении, и кроме того, имеют собственные атрибуты:
# 	BookPublisher – num_authors (количество авторов).
# 	NewspaperPublisher– num_pages (количество страниц в газете).


# Пример использования:
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")

# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")

# Вывод:
# Готовим "Справочник писателя" к публикации в АБВГД Пресс (Москва)
# Передаем рукопись 'Приключения Чебурашки', написанную автором В.И. Пупкин в издательство Важные Книги (Самара)
# Печатаем свежий номер со статьей "Новая версия Midjourney будет платной" на главной странице в издательстве Московские вести (Москва)

class Publisher:
    """
    Родительский класс издательства
    """
    def __init__(self, name: str, location: str) -> None:
        """
        Конструктор издательства
        name: Название издательства
        location: Расположение издательства
        """
        self.name = name
        self.location = location

    def get_info(self) -> str:
        """
        Получение информации об издательстве
        return: Строка с информацией о издательстве
        """
        return f"{self.name} ({self.location})"
    
    def publish(self, message: str) -> None:
        """
        Публикация информации
        message: Текст для публикации
        """
        print(f'Готовим "{message}" к публикации в {self.get_info()}')

class BookPublisher(Publisher):
    """
    Книжное издательство
    """
    def __init__(self, name: str, location: str, num_authors: int) -> None:
        """
        Конструктор книжного издательства
        name: Название издательства
        location: Расположение издательства
        num_authors: Количество авторов
        """
        super().__init__(name, location)
        self.num_authors = num_authors
    
    def publish(self, title: str, author: str) -> None:
        """
        Публикация книги
        title: Название книги
        author: Автор книги
        """
        print(f'Передаем рукопись "{title}", написанную автором {author} в издательство {self.get_info()}')
    

class NewspaperPublisher(Publisher):
    """
    Газетное издательство
    """
    def __init__(self, name: str, location: str, num_pages: int) -> None:
        """
        Конструктор газетного издательства
        name: Название издательства
        location: Расположение издательства
        num_pages: Количество страниц в газете
        """
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, article: str) -> None:
        """
        Публикация статьи в газете
        article: Текст статьи
        """
        print(f'Печатаем свежий номер со статьей "{article}" на главной странице в издательстве {self.get_info()}')



# Пример использования:
publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")

# Вывод:
# Готовим "Справочник писателя" к публикации в АБВГД Пресс (Москва)
# Передаем рукопись "Приключения Чебурашки", написанную автором В.И. Пупкин в издательство Важные Книги (Самара)
# Печатаем свежий номер со статьей "Новая версия Midjourney будет платной" на главной странице в издательстве Московские вести (Москва)





