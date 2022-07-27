lines = []
text = "life.txt"
def tail(text, n=14):
    with open(text, "r") as f:
        lines = f.readlines()
        print(len(lines))

    for line in lines[-1]:
        print(line)


tail(text,14)