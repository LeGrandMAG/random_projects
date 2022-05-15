import re

with open('life.txt', 'r') as file:
    f = file.readlines()


x = re.compile(r'\d+')
z = []
for d in f:
    o= x.match(d)
    m = o.group
    if o == None:
        print("no element")
    else:
        z.append(o)
        
print(z)

