import re
import codecs
pattern = r'динозавр'
pattern2 = r'Динозавр'
file_output = codecs.open("Коты.txt", 'w', 'utf-8')
with open('dino.txt', encoding='UTF-8') as file:
    for row in file:
        result = re.sub(pattern, "кот", row)
        result = re.sub(pattern2, "Кот", result)
        file_output.write(result + "\r\n")
file_output.close()
