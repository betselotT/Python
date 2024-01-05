def strings(lettersOne, lettersTwo):
    lettersOne = [letter.lower() for letter in lettersOne]
    lettersTwo = [letter.lower() for letter in lettersTwo]
    if lettersOne < lettersTwo:
        return -1
    elif lettersOne == lettersTwo:
        return 0
    else:
        return 1


inputOne = input().split()
inputTwo = input().split()
result = strings(inputOne, inputTwo)
print(result)