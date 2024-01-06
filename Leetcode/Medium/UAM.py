class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        arr = {}
        for i, j in logs:
            if i not in arr:
                arr[i] = set()
            arr[i].add(j)
        answer = [0] * k
        for i in arr:
            UAM = len(arr[i])
            answer[UAM - 1] += 1
        return answer