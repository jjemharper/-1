print('Пожалуйста, напишите слово')
a=input()
for i in range(len(a)//2):
    print(a[i])
for i in range(len(a)-1, len(a)//2-1,-1):
    print(a[i])
