import re

with open('life.txt', 'r') as file:
    f = file.readlines()


x = re.compile(r'\d+')

for d in f:
    o= x.findall(d)
    if o == None:
        print("no element")
    else:
        a

