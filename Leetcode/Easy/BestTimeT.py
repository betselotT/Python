class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maximum = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maximum = max(maximum, profit)
            else:
                left = right
            right += 1
        return maximum