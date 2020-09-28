#Даны два списка чисел. Посчитайте, сколько (уникальных)
#чисел содержится одновременно
#как в первом списке, так и во втором.
list_1=[]##объявление пустого списка
list_2=[]
import random ##подключение модуля случайных чисел  

for i in range(10):
     list_1.append(random.randint(10, 50))
     list_2.append(random.randint(1, 70))
     ##заполнение списка 10-ю случайными числами
print(list_1)     ## вывод списка 1

print(list_2)     ## вывод списка 2

print(set(list_1))

print(set(list_2))

print(len(set(list_1) & set(list_2)))
