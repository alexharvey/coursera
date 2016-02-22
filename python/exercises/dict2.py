fname = "/Users/alex/Downloads/mbox-short.txt"

fh = open(fname)
hours_dictionary = dict()
for line in fh:
    tokens = line.split()
    if len(tokens) < 2:
        continue
    if tokens[0] == 'From':
        t = tokens[5]
        hour = tokens[5].split(':')[0]
        if not hour in hours_dictionary:
            hours_dictionary[hour] = 1
        else:
            hours_dictionary[hour] += 1

keys = hours_dictionary.keys()
keys.sort()

for k in keys:
    print k, hours_dictionary[k]
