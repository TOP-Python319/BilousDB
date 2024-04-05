# Написать функцию с именем orth_triangle, которая вычисляет третью сторону прямоугольного треугольника по двум переданным.

# Функция принимает в качестве аргументов длины двух сторон: это могут быть два катета или один из катетов и гипотенуза. 
    
#     Для того чтобы обеспечить требуемую гибкость, понадобится создать три строго ключевых параметра, каждый со значением по умолчанию.
    
#     Длины стороны могут быть переданы в виде объектов int или float. 
#         С точки зрения аннотации, достаточно указать float — в подавляющем большинстве случаев это означает, что объекты int также допустимы.

# Функция возвращает длину третьей стороны треугольника или None, если вычисление невозможно.
    
#     Если вычисление возможно, то возвращается объект float.
    
#     Вычисление может оказаться невозможным при неправильной передаче аргументов. Например, если длина гипотенузы меньше длины катета.
#     Также вычисление невозможно или не имеет смысла, если в функцию передаётся три, а не два аргумента.

# Для выполнения расчётов используйте теорему Пифагора:
#     https://mateshka.ru/math/geometry/treugolnik.html

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> orth_triangle(cathetus1=3, hypotenuse=5)
#     4.0
#     >>> orth_triangle(cathetus1=8, cathetus2=15)
#     17.0
#     >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
#     None

def orth_triangle(*, cathetus1: float=0, cathetus2: float=0, hypotenuse: float=0) -> float | None:
    if cathetus1 < 0 or cathetus2 < 0 or hypotenuse < 0:
        return None 
    
    if hypotenuse == 0:
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    
    cat_sum = cathetus1 + cathetus2

    if hypotenuse > cat_sum:
        return (hypotenuse ** 2 - cat_sum ** 2) ** 0.5
    else:
        return None

print(orth_triangle(cathetus1=3, hypotenuse=5))
#     4.0
print(orth_triangle(cathetus1=8, cathetus2=15))
#     17.0
print(orth_triangle(cathetus2=9, hypotenuse=3))
#     None
print(orth_triangle(cathetus1=8, cathetus2=9, hypotenuse=3))
#     None