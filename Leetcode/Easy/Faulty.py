class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if s[i] == 'i':
                ans.reverse()
            else:
                ans.append(s[i])
        return "".join(ans)