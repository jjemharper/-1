 
f = open("lala.txt","r",encoding="utf-8")
a = f.read().split()
text = []
for n in a:
    b = n.strip('.,<>/?""1234567890-=_+''""[]{}()*&^%$#@!;:|\...').lower()
    text.append(b)
nexText=""
for word in text:
    d=dict()
    for ch in word:
        if ch not in d:d[ch]=1
        else:d[ch]+=1
    for idx in range(len(word)):
        for i in range(d[word[idx]]):
            nexText+=word[idx]
    nexText+=' '
print(nexText)
