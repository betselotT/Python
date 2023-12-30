class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        arr = []
        for i in range(len(words)):
            arr.append(words[i][0])
        if "".join(arr) == s:
            return True
        else:
            return False