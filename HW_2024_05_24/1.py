# Задача 1. (инкапсуляция, свойства-геттеры, свойства-сеттеры, property)

# Создайте класс Money, у которого есть:

#     конструктор __init__,
#         принимающий 2 аргумента: 
#             dollars, cents. По входным аргументам вам необходимо создать атрибут экземпляра total_cents. 
 
#     свойство-геттер dollars,
#         которое возвращает количество имеющихся долларов;
 
#     свойство-сеттер dollars,
#         которое принимает целое неотрицательное число — количество долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents,
#         при этом значение центов должно сохранятся.
#         В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";
 
#     свойство геттер cents,
#         которое возвращает количество имеющихся центов;
 
#     свойство сеттер cents,
#         которое принимает целое неотрицательное число меньшее 100
#         количество центов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents,
#         при этом значение долларов должно сохранятся.
#         В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";
 
#     метод __str__,
#         который возвращает строку вида "Ваше состояние составляет {dollars} долларов {cents} центов".
#         Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами

# В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!


class Money:
    def __init__(self, dollars, cents):
        self.total_cents = cents + (dollars * 100)

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if not isinstance(value, int) or value < 0:
            print('Error dollars')
        else:
            self.total_cents = self.total_cents - self.dollars * 100 + value * 100

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if not isinstance(value, int) or value < 0 or value > 99:
            print('Error cents')
        else:
            self.total_cents = self.total_cents - self.cents + value

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
    
    
# Пример работы:
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

# Вывод:
# Ваше состояние составляет 101 долларов 99 центов
# 101 99
# 10199
# Ваше состояние составляет 666 долларов 99 центов
# Ваше состояние составляет 666 долларов 12 центов




