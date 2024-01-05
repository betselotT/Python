def nextRound(k, nums):
    count = 0
    threshold_score = nums[k - 1]
    for score in nums:
        if score >= threshold_score and score > 0:
            count += 1
    return count

n, k = map(int, input().split())
scores = list(map(int, input().split()))

result = nextRound(k, scores)
print(result)