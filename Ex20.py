#Дан текст (много строк в одном вводе) состоящий из нескольких строки.
#Выведите слово, которое в этом тексте встречается чаще всего.
#Если таких слов несколько, выведите последнее.

#Задачу необходимо решить с использованием словаря.

mydictionary = {}
for i in range(int(input('Введите число строк в тексте:'))):
    line = input('Введите строку:').split()
    for word in line:
        mydictionary[word] = mydictionary.get(word, 0) + 1
print('Частотный словарь:')        
for k,v in mydictionary.items(): print(k, v)

print('Чаще всего встречается слово:') 
max_count = max(mydictionary.values())
most_frequent = [k for k, v in mydictionary.items() if v == max_count]
print(min(most_frequent))
