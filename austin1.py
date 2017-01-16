def name(title):
    with open (title+'.txt', 'r') as f:
       text = f.read()
       words = text.split(' ')
    return words
def ous():
    words = name("austin")
    b = 0
    c = 0
    for i, word in enumerate (words):
      if words[i].count("ous"):
       b = b + len(words[i])
       c = c + 1
    print(b / c)
    print(c)
 
ous()
