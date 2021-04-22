"""
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

Формат ввода, который используют Малевийцы:
треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b
где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности

"""
form=input()
if form == 'треугольник':
    a,b,c=(float(input()) for i in  range(3))
    p = (a + b + c) / 2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif form=='прямоугольник':
    print((float(input()))*(float(input())))
elif form=="круг":
    print((float(input())**2)*3.14)