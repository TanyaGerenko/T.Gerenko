#Дана строка.
# 1) выведите третий символ этой строки.
# 2) выведите предпоследний символ этой строки.
# 3) выведите первые пять символов этой строки.
# 4) выведите всю строку, кроме последних двух символов.
# 5) выведите все символы с четными индексами (считая, что индексация начинается с 0,
#    поэтому символы выводятся начиная с первого).
# 6) выведите все символы с нечетными индексами,то есть начиная со второго символа строки.
# 7) выведите все символы в обратном порядке, выведите все символы строки
#    через один в обратном порядке, начиная с последнего.
# 8) выведите длину данной строки.
#Для выполнения этого задания необходимо использовать индексы,
#срезы и функцию len(). Циклы и оператор if здесь не нужны.
string=input("Введите строку:")
print(string)
print("Третий символ этой строки.",string[2])
print("Предпоследний символ этой строки.",string[-2])
print("Первые пять символов этой строки.",string[:5])
print("Вся строка, кроме последних двух символов.",string[:-2])
print("Все символы с четными индексами.",string[::2])
print("Все символы с нечетными индексами.",string[1::2])
print("Все символы в обратном порядке.",string[::-1])
print("Все символы через один в обратном порядке.",string[::-2])
length = len(string)
print("Длина этой строки.",length)
