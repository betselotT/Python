def matrix(nums):
    for i in range(5):
        for j in range(5):
            if nums[i][j] == 1:
                moves = abs(i - 2) + abs(j - 2)
                return moves


nums = [list(map(int, input().split())) for _ in range(5)]
result = matrix(nums)
print(result)