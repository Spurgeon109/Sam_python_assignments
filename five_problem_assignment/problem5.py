import re


for_names = '^[A-Z][a-z]+\s[A-Z][a-z]+$'
for_addresses = '^\d{3}\s[A-Z][a-z]+\sSt.,\s[A-Z][a-z]+\s[A-Z]{2}\s\d{5}$'
for_mobilenos = '^\d{3}-\d{3}-\d{4}$'
d = {1:for_names,  2:for_addresses, 3:for_mobilenos}
f = open('data.txt', 'r')
c = int(input('''
       1) Enter 1 for printing names
       2) Enter 2 for printing addresses
       3) Enter 3 for printing mobile numbers
       4) Enter 4 to replace Dave with John and print.
'''))

for l in f.readlines():
    if c == 4:
        if re.search('\Dave', l):
            x = l.replace('Dave', 'John')
            print(x)
    elif re.match(d[c], l):
        print(l)