line = input('Input a word:')
n = len(line)-1
for i in range(len(line)):
    print(line[n::])
    n = n - 1
