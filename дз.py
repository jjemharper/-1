from os import  listdir
from os.path import  isfile
mypath=listdir('C:/Users/admin/Documents/учеба/прога/папки')
q=0
for i in mypath:
     if  not isfile(i):
        a=i.split(' ')
        if len(a)>=2:
            q+=1
 
print(q)
