class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        for i in range(n // 2):
            operations += n - (2 * i + 1)
        return operations