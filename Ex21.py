#Написать функцию arithmetic, принимающую 3 аргумента:
#первые 2 - числа, третий - операция, которая должна быть произведена над ними.
#Функция должна вернуть результат вычислений зависящий от третьего аргумент:
#    + сложить их;  -  вычесть; *  умножить; /  разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(a,b,c):
        if c=='+':
            return a+b
        elif c=='-':
            return a-b
        elif c=='*':
            return a*b
        elif c=='/':
            return a/b
        else:
            return "Неизвестная операция"

        
print("+:",arithmetic(12,56.9,'+'))
print("-:",arithmetic(92.8,56.9,'-'))
print("*:",arithmetic(12.89,10,'*'))
print("/:",arithmetic(100,30,'/'))
print(arithmetic(12,4,'^')) 
      
