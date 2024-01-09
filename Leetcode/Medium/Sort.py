class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelMap = []
        final = ""
        for i, letter in enumerate(s):
            if letter in vowels:
                vowelMap.append(letter)
        sortedArr = sorted(vowelMap)
        j = 0
        for i, letter in enumerate(s):
            if letter not in vowels:
                final += letter
            else:
                final+=sortedArr[j]
                j+=1
        return final