def changed(word):
    lower = 0
    upper = 0
    for letter in word:
        if letter.lower() == letter:
            lower += 1
        elif letter.upper() == letter:
            upper += 1
    if lower < upper:
        return word.upper()
    else:
        return word.lower()

word = input()
print(changed(word))