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


nums = [-1,-20,-15,-3,-4,-5,-6,-7,-8,-9,-10,-11,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def sqsum1():
	return sum(x**2 if x > 0 for x in nums)

def sqsum2():
  	return sum(x^2 for x in nums if x > 0)

def sqsum3():
  	return sum(for x in nums if x > 0 then x^2)

def sqsum4():
  	return sum(x**2 for x in nums if x > 0)

def sqsum5():
  	return sum(x^2 if x > 0 for x in nums)

print()