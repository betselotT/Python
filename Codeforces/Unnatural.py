def unnatural(words):
    V = ['a', 'e']
    C = ['b', 'c', 'd']
    arr = []
    for i in range(len(words)):
        if words[i] in V:
            if words[i - 1] in C and words[i + 1] not in C:
                arr.append(words[i - 1])
                arr.append(words[i])
            elif words[i - 1] in C and words[i + 1] in C:
                arr.append(words[i + 1])
                arr.append(words[i])
                arr.append(words[i - 1])
            else:
                break
    print(arr)
# ['b', 'a', 'c', 'e', 'd', 'b', 'a', 'b']

n = int(input())
while n:
    count = int(input())
    words = list(map(str, input().split()))
    unnatural(words)
    n-=1