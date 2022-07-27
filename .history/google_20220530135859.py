lines = []
text = "life.txt"
def tail(text, n=14, lines):
    with open(text, "r") as f:
        lines = f.readlines()
        print(len(lines))


tail(text,14, lines)