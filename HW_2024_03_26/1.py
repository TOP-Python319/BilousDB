# Описать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного факториала.
# Двойной факториал числа n обозначается n!! и определяется как произведение всех натуральных чисел в отрезке [1, n], имеющих ту же чётность что и n.

# Вход: 6
# Выход: 48

# Вход: 5
# Выход: 15

# Вход: 2
# Выход: 2

# Вход: 4
# Выход: 8

def double_fact(n: int) -> int | None:
    if n < 0:
        return None
    if n == 0:
        return 1
    if n == 1:
        return 1  # базовый случай, выход из функции
    else:
        return n * double_fact(n - 2) # рекурсивный случай, функция вызывает сама себя


print(double_fact(6))
# 48
print(double_fact(5))
# 15
print(double_fact(2))
# 2
print(double_fact(4))
# 8 
print(double_fact(-3))
# None
print(double_fact(0))
# 1
print(double_fact(1))
# 1
print(double_fact(9))
# 945

    