class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for i in s:
            if i == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1
        return count

    answer = []
    for i in range(len(nums)):
        if (i == 0 or i % 2 == 0):
            element = str(nums[i]) * (i + 1)
            answer.append(element)
    print(answer)