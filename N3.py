path = '/Users/handaru/Documents/code/textfix.txt'
f = open(path)
readData = f.read()
f.close()
readData = readData.lower()
words = {}
for word in readData.split():
    words[word] = words.get(word, 0) + 1
print(words.items())
print(sorted(words.items(), key=lambda x:x[1],reverse=True))