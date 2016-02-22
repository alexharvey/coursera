fname = "/Users/alex/Downloads/mbox-short.txt"

fh = open(fname)
count = 0
addresses = list()
for line in fh:
    tokens = line.split()
    if len(tokens) < 2:
        continue
    if tokens[0] == 'From':
        addresses.append(tokens[1])
        count += 1
        print tokens[1]


print "There were", count, "lines in the file with From as the first word"
