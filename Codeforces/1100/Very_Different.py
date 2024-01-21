def difference(petya, vasya):
    arr = []
    for i in range(len(petya)):
        maximum = 0
        max_index = 0
        for j in range(len(vasya)):
            diff = abs(petya[i] - vasya[j])
            if diff > maximum:
                maximum = diff
                max_index = j
        ans = abs(petya[i] - maximum)
        arr.append(maximum)
        vasya.pop(max_index)
    return sum(arr)


n = int(input())
while n:
    nums = list(map(int, input().split()))
    petya = list(map(int, input().split()))
    vasya = list(map(int, input().split()))
    print(difference(petya, vasya))
    n -= 1
