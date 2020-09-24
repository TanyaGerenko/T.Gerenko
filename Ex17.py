#Дан список чисел. Определите, сколько в нем встречается различных (уникальных) чисел.
list_of_numbers=[]##объявление пустого списка
import random ##подключение модуля случайных чисел random  

for i in range(20):
     list_of_numbers.append(random.randint(1, 8))
     ##заполнение списка 20-ю случайными числами в диапазоне от 1 до 8
print(list_of_numbers)     ## вывод списка


print(len(set(list_of_numbers)))
