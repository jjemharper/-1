import re
import os
import codecs
import csv
 
 
from os import walk
 
f = []
for (dirpath, dirnames, filenames) in walk(os.path.dirname(__file__)+"/news"):
    f.extend(filenames)
    break
 
se_pattern = re.compile(r"(?<=<se>)[\s\S\w\W]*?(?=</se>)")
 
 
file_toWrite = open("Sentence_number.txt", 'w', encoding='utf-8')
for path in f:
    file = codecs.open(os.path.dirname(__file__)+"/news/"+path, 'r', encoding='windows-1251')
    text = file.read()
 
    words_number = se_pattern.findall(text)
    file_toWrite.write(path + "\t" + str(len(words_number)) + "\n")
 
file_toWrite.close()
