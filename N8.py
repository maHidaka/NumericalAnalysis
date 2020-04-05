import numpy as np

path = '/Users/handaru/Documents/code/text.txt'
f = open(path)
readData = f.read()
f.close()
rawData = []
for a,b,c in zip(readData [0::1] , readData [1:][0::1], readData [2:][0::1]):
    rawData.append(a+b+c)
char_set = { x for x in rawData }
char_freq = { x : rawData.count(x) for x in char_set }
char_freq = sorted(char_freq.items(), key=lambda x:x[1],reverse=True)


char_freq =  dict(char_freq)

char_sum = sum(char_freq.values())

for k in char_freq.keys():
    p = char_freq[k] / char_sum
    char_freq[k] = p

key = list(char_freq.keys())
val = list(char_freq.values())
sentence = ""
for i in range(100):
    word = np.random.choice(key,p = val)
    sentence += str(word)
print(sentence)