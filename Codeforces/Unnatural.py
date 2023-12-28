def unnatural(words):
    V = ['a', 'e']
    C = ['b', 'c', 'd']
    arr = []
    for i in range(len(words)):
        for j in range(1, len(words)):
            for k in range(2, len(words)):
                if words[i] in C and words[j] in V:
                    arr.append(words[i][j])
                elif words[i] in C and words[j] in V and words[k] in C:
                    arr.append(words[i][j][k])
    print(arr)
# ['b', 'a', 'c', 'e', 'd', 'b', 'a', 'b']

n = int(input())
while n:
    count = int(input())
    words = list(map(str, input().split()))
    unnatural(words)
    n-=1