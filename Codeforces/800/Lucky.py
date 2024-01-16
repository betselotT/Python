def lucky(word):
    numList = [int(x) for x in list(word)]
    firstSum = 0
    secondSum = 0
    for i in range(0, 3):
        firstSum += numList[i]
        secondSum += numList[i + 3]
    if (firstSum == secondSum):
        print("YES")
    else:
        print("NO")


n = int(input())
while n:
    s = input()
    lucky(s)
    n -= 1