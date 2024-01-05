def domino(n, m):
    num = m * n
    return num // 2


n, m = list(map(int,input().split()))
result = domino(n, m)
print(result)