#В единственной строке записан текст. Для каждого слова из данного текста
#подсчитайте, сколько раз оно встречалось в этом тексте.
#Задачу необходимо решить с использованием словаря.

s="dog and cat dog dog sun cat abd tree cat cat cat dog"
mydictionary = {}#создаем пустой словарь
for word in s.split():
    mydictionary[word] = mydictionary.get(word, 1) + 1
    
for k,v in mydictionary.items(): print(k, v) 
    
