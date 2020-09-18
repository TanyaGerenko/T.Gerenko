#Пользователь вводит, отдельно, строку `s` и один символ `ch`.
#Необходимо выполнить поиск в строке `s` всех символов `ch`.

#Для решения НУЖНО использовать только функцию `find()`(rfind()),
#операторы `if` и `for`(while). 
string=input("Введите строку:")
print(string)
ch=input("Введите символ:")
print(ch)

k=0
pos=len(string)
while string[:pos].rfind(ch)>0:
          pos=string[:pos].rfind(ch)
          print("pos=",pos)
          k+=1
          
print(k)
