def cap(word):
    first = word[0].upper()
    ans = first + word[1:]
    return ans

word = input("Enter a word: ")
print(cap(word))
