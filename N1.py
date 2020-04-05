import re
path = '/Users/handaru/Documents/code/text.txt'
f = open(path)
readData = f.read()
f.close()
print(readData)
readData = readData.lower()
char_set = { x for x in readData }
char_freq = { x : readData.count(x) for x in char_set }
print(sorted(char_freq.items(), key=lambda x:x[1],reverse=True))
