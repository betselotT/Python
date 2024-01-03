class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for i in range(n):
            result += mat[i][i]
            result += mat[i][n - i - 1]

        if n % 2 != 0:
            mid = n // 2
            result -= mat[mid][mid]

        return result
