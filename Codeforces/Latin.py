def latin(lines):
    a = 0
    b = 0
    c = 0
    for i in range(len(lines)):
        a += lines[i].count("A")
        b += lines[i].count("B")
        c += lines[i].count("C")
    if a != 3:
        print("A")
    elif b != 3:
        print("B")
    elif c != 3:
        print("C")

n = int(input())
while n:
    lines = []
    for _ in range(3):
        line = input()
        lines.append(line)
    latin(lines)
    n-=1