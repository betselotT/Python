def matrix(line1, line2, line3, line4, line5):
    num = 0
    for i in range(len(line1)):
        if line1[i] == 1:
            num = 1
        if line2[i] == 1:
            num = 1
        if line3[i] == 1:
            num = 1
        if line4[i] == 1:
            num = 1
        if line5[i] == 1:
            num = 1
    line3[2] = num
    return line3[2]
line1 = list(map(int,input().split()))
line2 = list(map(int,input().split()))
line3 = list(map(int,input().split()))
line4 = list(map(int,input().split()))
line5 = list(map(int,input().split()))
result = matrix(line1, line2, line3, line4, line5)
print(result)