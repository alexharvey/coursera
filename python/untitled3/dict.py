fname = "/Users/alex/Downloads/mbox-short.txt"

fh = open(fname)
addresses = dict()
for line in fh:
    tokens = line.split()
    if len(tokens) < 2:
        continue
    if tokens[0] == 'From':
        if not tokens[1] in addresses:
            addresses[tokens[1]] = 1
        else:
            addresses[tokens[1]] += 1

max = 0
email = ''
for k in addresses.keys():
    if addresses[k] > max:
        max = addresses[k]
        email = k

print email, max

