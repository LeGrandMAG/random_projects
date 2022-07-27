
text = "life.txt"
def tail(text, n=14):
    with open(text, "r") as f:
        lines = f.readlines()
    for line in lines(n):
        print(line)

tail(line,)