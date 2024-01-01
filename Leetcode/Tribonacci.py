class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        final = 0
        if n == 0:
            return first
        elif n == 1:
            return second
        elif n == 2:
            return third
        if n > 2:
            for _ in range(3, n + 1):
                final = first + second + third
                temp = third
                third = final
                first = second
                second = temp
        return final