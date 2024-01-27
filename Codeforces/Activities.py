def activities(first, second, third):
    dayone = first.split(" ")
    daytwo = second.split(" ")
    daythree = third.split(" ")
    high1 = max(dayone)
    high2 = max(daytwo)
    high3 = max(daythree)
    answer = int(high1) + int(high2) + int(high3)
    print(answer)


n = int(input("Enter a number"))
while n:
    inp = input("Enter the input: ")
    activities(inp)
    n-=1
