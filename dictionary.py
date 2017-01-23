import csv
import random
d={}
key_list = []
with open('words.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        key_list.append(row[0])
        d[row[0]] = row[1]
    print("Загадали слово, вот ваша подсказка: ")
    a = random.randrange(0, len(key_list), 1)
    print(d[key_list[a]])
    count = 0
    while(input() != key_list[a]):
        count+=1
        print("Вы использовали следующее количество попыток: ",count)
    count+=1
    print("You won the game!!! и угадали с ", count, " раза")
