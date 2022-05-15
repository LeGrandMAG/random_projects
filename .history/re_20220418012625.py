import re

with open('life.txt', 'r') as file:
    f = file.readlines()


x = re.compile(r'\d+')

for d in f:
    for i in d:
        x = d.re.search('[\d]')
        print(x)


