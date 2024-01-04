def tooLong(n, word):
    num = len(word)
    arr = []
    for i in range(n):
        if num <= 10:
            return word
        else:
            arr.append(word[0])
            arr.append(str(num - 2))
            arr.append(word[-1])
            return "".join(arr)

n = int(input())
while n:
    word = input()
    result = tooLong(n, word)
    print(result)
    n-=1