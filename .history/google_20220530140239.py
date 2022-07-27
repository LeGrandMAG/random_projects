lines = []
text = "life.txt"
def tail(text, n=13):
    with open(text, "r") as f:
        lines = f.readlines()

    for line in lines.pop(n):
        print(line)


tail(text,14)