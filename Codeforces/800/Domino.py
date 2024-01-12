def domino(n, m):
    num = m * n
    return num // 2


n, m = list(map(int,input("Enter n and m: ").split()))
result = domino(n, m)
print(result)
