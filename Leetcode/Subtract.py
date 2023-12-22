class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        digits = str(n)
        for i in digits:
            p *= int(i)
            s += int(i)
        return p - s