class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = sum(range(1, n + 1))
        s_one = 0

        for i in range(1, n + 1):
            total_sum -= i
            if s_one == total_sum:
                return i
            s_one += i

        return -1