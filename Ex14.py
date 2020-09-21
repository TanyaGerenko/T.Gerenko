#Дан список чисел. Определите, сколько в этом списке элементов,
#которые больше двух своих соседей (слева и справа) и выведите количество
#таких элементов. Крайние элементы списка никогда не учитываются,
#поскольку у них недостаточно соседей.
list_of_numbers=[]##объявление пустого списка
import random ##подключение модуля случайных чисел random mas=[]

for i in range(10):
     list_of_numbers.append(random.randint(0, 100))
     ##заполнение списка 10-ю случайными числами в диапазоне от 0 до 100
print(list_of_numbers)     ## вывод списка
k=0
for j in range(1,9) :
     if list_of_numbers[j]>list_of_numbers[j-1]and list_of_numbers[j]>list_of_numbers[j+1]:
           k+=1;
print("k=",k)          
