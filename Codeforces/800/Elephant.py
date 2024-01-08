def steps(num):
    count = 0
    if num % 5 == 0:
        return num // 5
    else:
        return (num // 5) + 1

num = int(input())
print(steps(num))
