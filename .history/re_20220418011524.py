with open('life.txt', 'r') as file:
    f = file.readlines()


for d in f:
    for i in d:
        
        s = d.count(2)
        print(s)



