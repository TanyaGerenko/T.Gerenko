#ДЗ-6
#Дано целое, положительное, ТРЁХЗНАЧНОЕ число.
#Например: 123, 867, 374. Необходимо его перевернуть.
#Например, если ввели число 123, то должно получиться на выходе ЧИСЛО 321.
#ВАЖНО! Работать только с числами.
#Строки, оператор IF и циклы использовать НЕЛЬЗЯ!
n = int(input("Ввести целое, положительное, ТРЁХЗНАЧНОЕ число."))
reversN=n%10*100+n//10%10*10+n//100;
print("reversN:", reversN)
