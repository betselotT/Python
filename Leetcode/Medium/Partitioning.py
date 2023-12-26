class Solution:
    def minPartitions(self, n: str) -> int:
        max = ''
        for i in range(len(n)):
            if n[i] > max:
                max = n[i]
        return int(max)