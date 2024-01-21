class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newArr = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in newArr:
                newArr.remove(s[left])
                left += 1
            newArr.add(s[right])
            ans = max(ans, right - left + 1)
        return ans