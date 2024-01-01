class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lowercase = set(string.ascii_lowercase)
        letters = set(sentence)

        return all(letter in letters for letter in lowercase)