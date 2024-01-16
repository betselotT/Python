class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = {}
        secondWord = {}

        for letter in s:
            firstWord[letter] = s.count(letter)
        for letter in t:
            secondWord[letter] = t.count(letter)
        return firstWord == secondWord