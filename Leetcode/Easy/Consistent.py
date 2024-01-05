class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedLetters = set(allowed)
        count = 0
        for i in words:
            isConsistent = True
            for j in i:
                if j not in allowedLetters:
                    isConsistent = False
                    break
            if isConsistent:
                count += 1
        return count