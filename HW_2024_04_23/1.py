# Ссылки по теме:
# https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D0%BA (что такое тип данных стек)
# https://ru.wikipedia.org/wiki/LIFO (что такое принцип LIFO)


# =========================================
# В этом задании вам предстоит реализовать свой стек (stack) — это упорядоченная коллекция элементов, 
# организованная по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

# Ваша задача реализовать класс Stack, у которого есть:

#   метод __init__() создаёт новый пустой стек. 
#     Параметры данный метод не принимает.
#     Создает атрибут экземпляра values, 
#     где будут в дальнейшем храниться элементы стека в виде списка (list), 
#     изначально при инициализации задайте значение атрибуту values, равное пустому списку;
 
#   метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает;
 
#   метод pop() удаляет верхний элемент из стека.
#     Параметры не требуются, метод возвращает элемент.
#     Стек изменяется.
#     Если пытаемся удалить элемент из пустого списка, 
#     необходимо вывести сообщение "Empty Stack";
 
#   метод peek() возвращает верхний элемент стека, но не удаляет его.
#     Параметры не требуются, стек не модифицируется.
#     Если элементов в стеке нет, 
#     распечатайте сообщение "Empty Stack",
#     верните None после этого;
 
#   метод is_empty() проверяет стек на пустоту.
#     Параметры не требуются, возвращает булево значение.
 
#   метод size() возвращает количество элементов в стеке.
#     Параметры не требуются, тип результата — целое число.


# =========================================
# Пример работы с экземпляром класса Stack:
# stack = Stack()
# stack.push(10)
# stack.push(12)
# stack.push(14)
# stack.size()
# # >>>: 3
# stack.is_empty()
# # >>>: False
# stack.peek()
# # >>>: 14
# stack.peek()
# # >>>: 14
# stack.pop()
# # >>>: 14
# stack.size()
# # >>>: 2
# stack.pop()
# # >>>: 12
# stack.pop()
# # >>>: 10
# stack.pop()
# # >>>: Empty Stack
# stack.peek()
# # >>>: Empty Stack
# stack.size()
# # >>>: 0
# stack.is_empty()
# # >>>: True



class Stack:

    def __init__(self):
        self.values = []  # Инициализация пустого списка для хранения элементов стека

    def push(self, item):
        self.values.append(item)  # Добавление нового элемента в конец списка

    def pop(self):
        if self.is_empty():  # Проверка на пустоту стека
            print("Empty Stack")
            return
        return self.values.pop()  # Удаление и возвращение последнего элемента списка (вершины стека)

    def peek(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        return self.values[-1]  # Возвращаем верхний элемент стека
    
    def is_empty(self):
        return len(self.values) == 0  # Проверяем, пуст ли стек
    
    def size(self):
        return len(self.values)  # Возвращаем количество элементов в стеке

# Пример использования:
stack = Stack()
stack.push(10)
stack.push(12)
stack.push(14)
print(stack.size())  # >>> 3
print(stack.is_empty())  # >>> False
print(stack.peek())  # >>> 14
print(stack.peek())  # >>> 14
print(stack.pop())  # >>> 14
print(stack.size())  # >>> 2
print(stack.pop())  # >>> 12
print(stack.pop())  # >>> 10
print(stack.pop())  # >>> Empty Stack
print(stack.peek())  # >>> Empty Stack
print(stack.size())  # >>> 0
print(stack.is_empty())  # >>> True
    

# Комментарий преподавателя:
# Отличное решение, вижу, что разобрались, оставлю пару замечаний:

# Хорошей практикой является добавление документации к классу и его методам.
# Это поможет другим разработчикам лучше понять,
# как использовать класс и что ожидать от его методов.

# Например, при попытке вызова метода peek() или pop() из пустого стека
# можно использовать исключение IndexError для более явного оповещения об ошибке.

# Добавление аннотаций типов к методам класса поможет лучше понять,
# какие типы данных ожидаются и возвращаются методами.