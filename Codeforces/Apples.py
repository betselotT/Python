def divide(n, weight):
    sum_hundred = weight.count(100)
    sum_twohundred = weight.count(200)
    if sum_hundred % 2 == 0 and (sum_twohundred % 2 == 0 or sum_hundred > 0):
        return 'YES'
    else:
        return 'NO'

n = int(input())
weight = list(map(int, input().split()))
answer = divide(n, weight)
print(answer)
