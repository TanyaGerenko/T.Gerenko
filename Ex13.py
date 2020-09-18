#Дана строка. Замените в этой строке все появления буквы `h` на букву `H`,
#кроме первого и последнего вхождения.

#Понадобятся: срезы, функция replace().
# замена `h` на `H`
string=input("Введите строку:")
print(string)
first=string.find("h")
last=string.rfind("h")
print("first=",first,"last=",last)
replaced_string = string[first+1:last-1].replace("h", "H")
edited_string=string[0:first+1]+replaced_string+string[last:len(string)]
print(edited_string)     
