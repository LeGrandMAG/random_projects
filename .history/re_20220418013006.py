import re

with open('life.txt', 'r') as file:
    f = file.readlines()


x = re.compile(r'\d+')
z = []
for d in f:
    o= x.search(d)
    if o == None:
        print("no element")
    else:
        z.append(o)
        
print(z)

