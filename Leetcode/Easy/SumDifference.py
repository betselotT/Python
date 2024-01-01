class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        leftSum = 0
        rightSum = sum(nums)

        for num in nums:
            rightSum -= num
            answer.append(abs(leftSum - rightSum))
            leftSum += num
        return answer