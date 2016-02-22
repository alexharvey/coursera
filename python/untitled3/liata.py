fname = '/Users/alex/Downloads/romeo.txt'
fh = open(fname)
lst = list()
words = list()
for line in fh:
    for word in line.split():
        if not word in words:
            words.append(word)

words.sort()

for w in words:
    print w,