def team(petya, vasya, tonya):
    count = 0
    if petya + vasya + tonya >= 2:
        count += 1
    print(count)

n = int(input())
while n:
    p = int(input())
    v = int(input())
    t = int(input())
    n-=1
team(p, v, t)