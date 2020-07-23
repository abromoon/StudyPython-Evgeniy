# https://stepik.org/lesson/3363/step/2?unit=1135

"""
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
"""

t = ''
n = ''
with open(r'texts/dataset_3363_2 (5).txt', 'r') as file:
    line = file.readline().strip()

with open('texts/answer.txt', 'w') as file:
    print(line)

    for ch in line:
        if ch.isalpha():
            if t != '':
                file.write(t * int(n))
                n = ''
                t = ch
            else:
                t = ch

        else:
            n += ch
    file.write(t * int(n))

