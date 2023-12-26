class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)[::-1]
        number = str(x)
        if num == number:
            return True