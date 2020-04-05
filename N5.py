path = '/Users/handaru/Documents/code/text.txt'
f = open(path)
readData = f.read()
f.close()
readData = readData.lower()
rawData = []
for a,b,c in zip(readData [0::1] , readData [1:][0::1], readData [2:][0::1]):
    rawData.append(a+b+c)
char_set = { x for x in rawData }
char_freq = { x : rawData.count(x) for x in char_set }
print(sorted(char_freq.items(), key=lambda x:x[1],reverse=True))