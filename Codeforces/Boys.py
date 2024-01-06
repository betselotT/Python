def alternate(boys, girls):
    arr = [''] * (boys + girls)
    for i in range(boys):
        arr.append('B')
        arr.append('G')

    return arr

b, g = map(int, input().split())
print(alternate(b, g))