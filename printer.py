from asyncore import read
from time import sleep


with open('random_projects\life.txt', 'r') as mylife:

    t= mylife.readlines()
    tee =[]
    for love in t:
        if love != '\n':
            tee.append(love)


for i in tee:
    print(i, end='')

    sleep(1)
