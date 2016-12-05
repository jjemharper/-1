f = open("C:/Users/admin/Documents/учеба/article.txt", "r", encoding = "utf(8)")
s = 0
a = 0
for line in f:
    arr = line.split()
    s = s + len(arr)
    for i in arr:
        if len(i)>10:
             a = a + 1
f.close()
b = a/s*100
print(b , "%")
    
