#Написать функцию square, принимающую 1 аргумент — сторону квадрата,
#и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
#площадь квадрата и диагональ квадрата.
import math

def square(a):

    p = 4 * a
    s = a ** 2
    diag = math.hypot(a, a)
    return (p, s, diag)

a = int(input("Введите сторону квадрата: "))       
print("Сторона квадрата=",a,"Периметр=",square(a)[0],";Площадь=",square(a)[1])
print("Диагональ=",square(a)[2])
