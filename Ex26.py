#Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).  В качестве параметров, функция получает десятичное число и систему счисления.
#Возвращает строку - результат перевода десятичного числа.

def ConvertNumber(n,base):
    D=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    MyStack=[]
    MyNumber=[]
    while n>0:
          MyStack.append(n%base)
          n=n//base
    print(MyStack)
    while len(MyStack)>0:
          x=MyStack.pop()
          if x>10:
              MyNumber.append(D[x-1])
          else:
              MyNumber.append(x)
    print(MyNumber)
    str1 = ''.join(str(e) for e in MyNumber)
    return str1
    
n=int(input("n="))
base=int(input("base="))
print(ConvertNumber(n,base))

