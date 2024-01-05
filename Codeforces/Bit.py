X = 0
def bit(operations):
    global X
    if operations == '++X' or operations == 'X++':
        X += 1
    elif operations == '--X'  or operations == 'X--':
        X -= 1
    return X

n = int(input())
while n:
    operations = input()
    result = bit(operations)
    n-=1
print(result)