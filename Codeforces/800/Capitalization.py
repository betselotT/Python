def cap(word):
    first = word[0].upper()
    ans = first + word[1:]
    return ans

word = input()
print(cap(word))