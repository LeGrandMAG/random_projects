import re 
lines = []
text = "life.txt"
def tail(text, n=14):
    with open(text, "r") as f:
        lines = f.readlines()

    for line in lines[len(lines)-n:]:
        print(line)


######################################
def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])

def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))

def parse3():
    for line in open("log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))

def parse4():
    for line in open("log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))
  
def parse5():
    for line in open("log.txt"):
        print(re.split("\[|\]", line)[1])

parse4()