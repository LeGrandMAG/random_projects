with open('life.txt', 'r') as file:
    f = file.readlines()


for d in f:
    for i in d:
        if i == "I":
            s = d.count(i)
            print(s)



