
text = "life.txt"
def tail(text, n=14):
    with open(text, "r") as f:
        lines = f.readlines()
    print(lines.pop(n))

print(tail(text))