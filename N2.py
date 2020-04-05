import re
path = '/Users/handaru/Documents/code/'
fpath = '/Users/handaru/Documents/code/text.txt'
f = open(fpath)
readData = f.read()
f.close()
readData = readData.lower()
print(readData)
with open(path+"textfix.txt", mode='w') as f:
    readData = re.sub(re.compile('"'), ' ', readData)
    f.write(re.sub(re.compile("[!-/:-@[-`{-~]"), ' ', readData))
