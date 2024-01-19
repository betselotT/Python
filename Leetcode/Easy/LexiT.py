class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        new = list(s)
        left = 0
        right = len(new) - 1
        while left < right:
            if new[left] != new[right]:
                if new[left] < new[right]:
                    new[right] = new[left]
                elif new[left] > new[right]:
                    new[left] = new[right]
            left += 1
            right -= 1
        return "".join(new)