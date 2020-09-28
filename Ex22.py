#Написать функцию is_year_leap, принимающую 1 аргумент — номер года,
#и возвращающую True,если год високосный, и False иначе.
def is_year_leap(year):
        
    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False

year = int(input("Введите год: "))       
if is_year_leap(year):
    print(year,"-високосный")
else:
    print(year, "не високосный")
