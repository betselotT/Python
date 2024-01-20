def maximumStrongPairXor(self, nums: List[int]) -> int:
    left = 0
    right = 0
    result = []
    maximum = 0
    while left < len(nums):
        while right < len(nums) and abs(nums[left] - nums[right]) <= min(nums[left], nums[right]):
            result.append((nums[left], nums[right]))
            right += 1
        left += 1
        right = left
    for i in range(len(result)):
        maximum = max(maximum, result[i][0] ^ result[i][1])
    return maximum