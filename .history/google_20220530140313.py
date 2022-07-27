lines = []
text = "life.txt"
def tail(text, n=14):
    with open(text, "r") as f:
        lines = f.readlines()

    for line in lines[]:
        print(line)


tail(text,14)