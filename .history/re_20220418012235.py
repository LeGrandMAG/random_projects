import re

with open('life.txt', 'r') as file:
    f = file.readlines()


for d in f:
    for i in d:
        d.search('[\d]')
        if i == "I":
            print(d)
            s = d.count(i)
            print(s)



