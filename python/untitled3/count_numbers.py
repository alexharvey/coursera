import re

fname = '/Users/alex/Downloads/regex_sum_170689.txt'
fh = open(fname)
lst = list()
total = 0
for line in fh:
    int_list = [int(s) for s in re.findall('\d+', line)]
    total = total + sum(int_list)

print total

