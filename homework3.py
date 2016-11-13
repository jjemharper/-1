arr = [ ]
while True:
    word = input('Input a word: ')
    if word==(' '): break
    elif word.endswith ('tur'):
        arr.append(word)
print (arr)
