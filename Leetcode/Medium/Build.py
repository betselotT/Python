class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        stack = []
        j = 0
        for i in range(1, max(target) + 1):
            stack.append(i)
            arr.append("Push")
            if j < len(target) and target[j] == i:
                j += 1
            else:
                stack.pop()
                if j < len(target):
                    arr.append("Pop")
        return arr