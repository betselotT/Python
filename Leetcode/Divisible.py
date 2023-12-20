class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        answer = 0
        for i in range(1, n + 1):
            if i % m != 0:
                answer += i
            else:
                answer -= i
        return answer