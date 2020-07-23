# https://stepik.org/lesson/3363/step/3?unit=1135

"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
"""

words = []
d = {}
with open('dataset_3363_3 (2).txt', 'r') as file:
    lines = file.readlines()

for i in lines:
    words += i.lower().split()
print(lines)
print(words)
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
k = 0
w = ''
for key in d:
    if d[key] > k:
        k, w = d[key], key
    elif d[key] == k:
        if key > w:
            k, w = d[key], key

print(w, k)