def helpful(number):
    num = sorted(number)
    return '+'.join(map(str, num))

num = list(map(int,input().split("+")))
result = helpful(num)
print(result)