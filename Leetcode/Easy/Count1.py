class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        number = str(num)
        for i in number:
            if num % int(i) == 0:
                count += 1
        return count