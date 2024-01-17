class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index = 0
        curr = 1
        arr = []
        while index < len(target):
            while curr != target[index]:
                arr.append('Push')
                arr.append('Pop')
                curr += 1
            arr.append('Push')
            index += 1
            curr += 1
        return arr