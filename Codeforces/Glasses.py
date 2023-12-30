def glasses(count, amount):
    sum_girl = 0
    sum_boy = 0
    for i in range(0, len(amount), 2):
        sum_boy += amount[i]
    for i in range(1, len(amount), 2):
        sum_girl += amount[i]

    if sum_boy == sum_girl:
        return "YES"
    else:
        return "NO"

n = int(input())
while n:
    count = int(input())
    amount = list(map(int,input().split()))
    result = glasses(count, amount)
    n-=1
    print(result)