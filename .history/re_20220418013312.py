import re

with open('life.txt', 'r') as file:
    f = file.readlines()


x = re.compile(r'\d+')
z = []
for d in f:
    o= x.match(d)
    m = o.group()
    if m == None:
        print("no element")
    else:
        z.append(m)
        
print(z)

