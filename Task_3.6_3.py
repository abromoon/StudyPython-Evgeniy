# https://stepik.org/lesson/3378/step/3?unit=961

"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""

import requests
k = 1
with open('texts/dataset_3378_3 (3).txt', 'r') as f:
    r = requests.get(f.readline().strip())
    print(r.text, k)
    k += 1
while True:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
    if r.text.splitlines()[0].split()[0] == 'We':
        print(r.text)
        file = open('newfile.txt', 'w')
        file.write(str(r.text))
        file.close()
        break
    print(r.text, k)
    k += 1