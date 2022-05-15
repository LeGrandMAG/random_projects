import re

with open('life.txt', 'r') as file:
    f = file.readlines()


x = re.compile(r'\d+')
z = []
for d in f:
    o= x.findall(d)
    if o == None:
        print("no element")
    else:
        for r in o:
            z.append(r)
        
for q in z:
    print(q, end='.')

