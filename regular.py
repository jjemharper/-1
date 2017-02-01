import re
pattern = r'[сС][Ъъ][Ее][\w]*'
with open('eat.txt', encoding='UTF-8') as file:
    for row in file:
        result = re.findall(pattern, row)
        for res in result:
            print(res)
