def chat(word):
    w = ['h', 'e', 'l', 'l', 'o']
    wo = list(word)
    left = 0
    right = 0
    arr = []
    while left < len(wo) and right < len(w):
        if wo[left] != w[right]:
            left += 1
        else:
            if wo[left] not in arr:
                arr.append(wo[left])
            right += 1
            left += 1
    return arr

word = input()
print(chat(word))