#ДЗ5
#В школе решили набрать три новых математических класса.
#Так как занятия по математике у них проходят в одно и то же время,
#было решено выделить кабинет для каждого класса и купить в них новые парты.
#За каждой партой может сидеть не больше двух учеников.
#Известно количество учащихся в каждом из трёх классов.
#Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
#Программа получает на вход три натуральных числа:
#          количество учащихся в каждом из трех классов.
class1 = int(input("Сколько Учеников в первом классе? "))
class2 = int(input("Сколько Учеников во втором классе? "))
class3 = int(input("Сколько Учеников в третьем классе? "))
k1=class1//2+class1%2
k2=class2//2+class2%2
k3=class3//2+class3%2
print("Для первого класса нужно закупить  ", k1, "парт")
print("Для второго класса нужно закупить  ", k2, "парт")
print("Для третьего класса нужно закупить  ", k3, "парт")
print("Всего нужно купить:", k1+k2+k3, "парт")