import re

with open('life.txt', 'r') as file:
    f = file.readlines()


for d in f:
    for i in d:
        x = d.search('[\d]')
        print


