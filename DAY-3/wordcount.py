file = open("textfile.txt", "rt")
data = file.read()
words = data.split()
lines = 0


ListLine=data.split("\n")

for i in ListLine:
    if i:
        lines +=1

print('number of characters',len(data))
print('Number of words in text file :', len(words))
print('number of lines:',lines)