#По данному натуральному числу N найдите наибольшую целую степень двойки,
#не превосходящую N.
#Выведите показатель степени и саму степень.
#Операцию возведения в степень,
#а так же функцию возведения в степень использоваться НЕЛЬЗЯ!
#50     5 32      2 ** 5 = 32
#10     3 8       2 ** 3 = 8
#8      3 8       2 ** 3 = 8
#1025    10 1024     2 ** 10 = 1024
#15431543  23 8388608   2 ** 23 = 8388608

n=int(input("Введите целое число:"))
i=1
j=0
while i<n:
          j+=1
          i*=2
i//=2
j-=1
print(n,"Показатель степени=",j,"->степень 2->",i,end=" ")     
print("2**",j,"=",2**j)
