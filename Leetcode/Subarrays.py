class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        odd = len(arr)

        for i in range(odd):
            for j in range(i, odd, 2):
                total += sum(arr[i:j+1])
        return total