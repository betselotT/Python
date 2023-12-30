class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        arr = []
        for i in range(len(words)):
            arr.append(words[i][0])
        answer = "".join(arr)
        if answer == s:
            return True
        else:
            return False